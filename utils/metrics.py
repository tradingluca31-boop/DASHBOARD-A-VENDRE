"""
📊 METRICS CALCULATOR - Trading Dashboard Pro
COMPLETE institutional-grade trading metrics (30+ metrics)
"""

from typing import List, Dict, Optional
import pandas as pd
import numpy as np
from scipy import stats


class MetricsCalculator:
    """
    Calculate ALL institutional-grade trading metrics.

    Includes:
    - Performance: ROI, P&L, CAGR, Profit Factor, Expectancy
    - Risk: Sharpe, Sortino, Calmar, Max DD, VaR, CVaR
    - Trade Stats: Win Rate, Avg Win/Loss, Best/Worst, W/L Ratio
    - FTMO: Compliance checks
    - Advanced: Recovery Factor, Ulcer Index, Pain Index, Kelly
    """

    def __init__(self, data: List[Dict], initial_balance: float = 10000.0):
        """
        Initialize calculator with checkpoint data.

        Args:
            data: List of checkpoint dictionaries (from training_stats.json)
            initial_balance: Starting account balance
        """
        self.data = data
        self.df = pd.DataFrame(data)
        self.initial_balance = initial_balance

        # Calculate returns if not present
        if "balance" in self.df.columns:
            self.df["returns"] = self.df["balance"].pct_change().fillna(0)
        elif "total_reward" in self.df.columns:
            # If only total_reward available, create balance
            self.df["balance"] = initial_balance + self.df["total_reward"]
            self.df["returns"] = self.df["balance"].pct_change().fillna(0)

    # ============================================
    # MAIN FUNCTION - GET ALL METRICS
    # ============================================

    def get_all_metrics(self) -> Dict[str, any]:
        """
        Get ALL 30+ metrics in one dictionary.

        Returns:
            Complete metrics dictionary with all calculations
        """
        if self.df.empty:
            return {}

        # Get last row for final values
        last_row = self.df.iloc[-1]
        final_balance = last_row.get("balance", self.initial_balance)

        # Calculate all metrics
        return {
            # ===== PERFORMANCE =====
            "roi_percent": ((final_balance - self.initial_balance) / self.initial_balance) * 100,
            "total_pnl": final_balance - self.initial_balance,
            "final_balance": final_balance,
            "initial_balance": self.initial_balance,
            "profit_factor": self._safe_get(last_row, "profit_factor", self.calculate_profit_factor()),
            "expectancy": self._safe_get(last_row, "expectancy", self.calculate_expectancy()),

            # ===== RISK METRICS =====
            "sharpe_ratio": self._safe_get(last_row, "sharpe_ratio", self.calculate_sharpe_ratio()),
            "sortino_ratio": self.calculate_sortino_ratio(),
            "calmar_ratio": self.calculate_calmar_ratio(),
            "max_drawdown_pct": self._safe_get(last_row, "max_drawdown_pct", self.calculate_max_drawdown()),
            "max_daily_loss_pct": self._safe_get(last_row, "max_daily_loss_pct", 0),
            "var_95": self.calculate_var(0.95),
            "cvar_95": self.calculate_cvar(0.95),

            # ===== TRADE STATS =====
            "total_trades": self._safe_get(last_row, "total_trades", 0),
            "winning_trades": self._safe_get(last_row, "winning_trades", 0),
            "losing_trades": self._safe_get(last_row, "losing_trades", 0),
            "win_rate": self._safe_get(last_row, "win_rate", self.calculate_win_rate()),
            "avg_win": self._safe_get(last_row, "avg_win", 0),
            "avg_loss": self._safe_get(last_row, "avg_loss", 0),
            "best_trade": self._safe_get(last_row, "best_trade", 0),
            "worst_trade": self._safe_get(last_row, "worst_trade", 0),
            "win_loss_ratio": self.calculate_win_loss_ratio(),
            "avg_trade_duration_hours": self._safe_get(last_row, "avg_trade_duration_hours", 0),

            # ===== FTMO COMPLIANCE =====
            "ftmo_max_dd_compliant": self._safe_get(last_row, "max_drawdown_pct", 0) < 10,
            "ftmo_daily_loss_compliant": self._safe_get(last_row, "max_daily_loss_pct", 0) < 5,
            "trading_days": self._estimate_trading_days(),

            # ===== ADVANCED METRICS =====
            "recovery_factor": self.calculate_recovery_factor(),
            "ulcer_index": self.calculate_ulcer_index(),
            "pain_index": self.calculate_pain_index(),
            "kelly_criterion": self.calculate_kelly_criterion(),

            # ===== EXTRA INFO =====
            "total_timesteps": self._safe_get(last_row, "timestep", len(self.df)),
            "cagr": self.calculate_cagr(),
        }

    # ============================================
    # HELPER FUNCTIONS
    # ============================================

    def _safe_get(self, row, key, default=0):
        """Safely get value from row with default"""
        return row.get(key, default) if isinstance(row, dict) else default

    def _estimate_trading_days(self) -> int:
        """Estimate number of trading days (rough estimate)"""
        # Assume each ~50 episodes = 1 day
        return max(1, len(self.df) // 50)

    # ============================================
    # PERFORMANCE METRICS
    # ============================================

    def calculate_profit_factor(self) -> float:
        """
        Calculate Profit Factor = Total Gains / Total Losses

        Returns:
            Profit factor
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        # Calculate P&L per period
        pnl = self.df["balance"].diff().fillna(0)
        gains = pnl[pnl > 0].sum()
        losses = abs(pnl[pnl < 0].sum())

        if losses == 0:
            return gains if gains > 0 else 0.0

        return gains / losses

    def calculate_expectancy(self) -> float:
        """
        Calculate Expectancy = (Win Rate × Avg Win) - (Loss Rate × Avg Loss)

        Returns:
            Expected profit per trade
        """
        if self.df.empty:
            return 0.0

        last_row = self.df.iloc[-1]
        win_rate = self._safe_get(last_row, "win_rate", 0) / 100
        loss_rate = 1 - win_rate
        avg_win = self._safe_get(last_row, "avg_win", 0)
        avg_loss = abs(self._safe_get(last_row, "avg_loss", 0))

        return (win_rate * avg_win) - (loss_rate * avg_loss)

    # ============================================
    # RISK METRICS
    # ============================================

    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.02) -> float:
        """
        Calculate annualized Sharpe Ratio.

        Args:
            risk_free_rate: Annual risk-free rate (default 2%)

        Returns:
            Sharpe ratio
        """
        if "returns" not in self.df.columns or len(self.df) < 2:
            return 0.0

        returns = self.df["returns"].values
        excess_returns = returns - (risk_free_rate / 252)  # Daily risk-free rate

        if np.std(excess_returns) == 0:
            return 0.0

        sharpe = np.mean(excess_returns) / np.std(excess_returns)
        return sharpe * np.sqrt(252)  # Annualize

    def calculate_sortino_ratio(self, risk_free_rate: float = 0.02) -> float:
        """
        Calculate Sortino Ratio (uses downside deviation only).

        Args:
            risk_free_rate: Annual risk-free rate

        Returns:
            Sortino ratio
        """
        if "returns" not in self.df.columns or len(self.df) < 2:
            return 0.0

        returns = self.df["returns"].values
        excess_returns = returns - (risk_free_rate / 252)

        # Downside deviation (only negative returns)
        downside_returns = excess_returns[excess_returns < 0]

        if len(downside_returns) == 0 or np.std(downside_returns) == 0:
            return 0.0

        sortino = np.mean(excess_returns) / np.std(downside_returns)
        return sortino * np.sqrt(252)  # Annualize

    def calculate_calmar_ratio(self) -> float:
        """
        Calculate Calmar Ratio = CAGR / Max Drawdown.

        Returns:
            Calmar ratio
        """
        max_dd = abs(self.calculate_max_drawdown())

        if max_dd == 0:
            return 0.0

        cagr = self.calculate_cagr()
        return cagr / max_dd

    def calculate_max_drawdown(self) -> float:
        """
        Calculate maximum drawdown percentage.

        Returns:
            Max drawdown as percentage (negative value)
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        # Calculate running maximum
        running_max = self.df["balance"].cummax()

        # Calculate drawdown
        drawdown = (self.df["balance"] - running_max) / running_max * 100

        return drawdown.min()  # Most negative value

    def calculate_cagr(self) -> float:
        """
        Calculate Compound Annual Growth Rate.

        Returns:
            CAGR as percentage
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        final_balance = self.df["balance"].iloc[-1]
        initial = self.initial_balance

        # Estimate years (assuming ~252 trading days per year or 1000 episodes per year)
        num_periods = len(self.df)
        years = max(0.1, num_periods / 1000)  # Rough estimate

        if years == 0 or initial == 0:
            return 0.0

        cagr = (((final_balance / initial) ** (1 / years)) - 1) * 100
        return cagr

    def calculate_var(self, confidence: float = 0.95) -> float:
        """
        Calculate Value at Risk (VaR).

        Args:
            confidence: Confidence level (default 95%)

        Returns:
            VaR as percentage
        """
        if "returns" not in self.df.columns or len(self.df) < 2:
            return 0.0

        returns = self.df["returns"].values
        var = np.percentile(returns, (1 - confidence) * 100)
        return var * 100  # Convert to percentage

    def calculate_cvar(self, confidence: float = 0.95) -> float:
        """
        Calculate Conditional Value at Risk (CVaR/Expected Shortfall).

        Args:
            confidence: Confidence level

        Returns:
            CVaR as percentage
        """
        if "returns" not in self.df.columns or len(self.df) < 2:
            return 0.0

        returns = self.df["returns"].values
        var_threshold = np.percentile(returns, (1 - confidence) * 100)

        # Average of returns below VaR
        tail_returns = returns[returns <= var_threshold]

        if len(tail_returns) == 0:
            return 0.0

        cvar = tail_returns.mean()
        return cvar * 100

    # ============================================
    # TRADE STATS
    # ============================================

    def calculate_win_rate(self) -> float:
        """
        Calculate win rate percentage.

        Returns:
            Win rate as percentage (0-100)
        """
        if self.df.empty:
            return 0.0

        last_row = self.df.iloc[-1]
        winning = self._safe_get(last_row, "winning_trades", 0)
        total = self._safe_get(last_row, "total_trades", 0)

        if total == 0:
            return 0.0

        return (winning / total) * 100

    def calculate_win_loss_ratio(self) -> float:
        """
        Calculate Win/Loss Ratio = Avg Win / Avg Loss

        Returns:
            Win/Loss ratio
        """
        if self.df.empty:
            return 0.0

        last_row = self.df.iloc[-1]
        avg_win = self._safe_get(last_row, "avg_win", 0)
        avg_loss = abs(self._safe_get(last_row, "avg_loss", 0))

        if avg_loss == 0:
            return avg_win if avg_win > 0 else 0.0

        return avg_win / avg_loss

    # ============================================
    # ADVANCED METRICS
    # ============================================

    def calculate_recovery_factor(self) -> float:
        """
        Calculate Recovery Factor = Net Profit / Max Drawdown (in dollars).

        Returns:
            Recovery factor
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        net_profit = self.df["balance"].iloc[-1] - self.initial_balance

        # Max drawdown in dollars
        running_max = self.df["balance"].cummax()
        drawdown_dollars = (self.df["balance"] - running_max).min()

        if drawdown_dollars == 0:
            return net_profit if net_profit > 0 else 0.0

        return abs(net_profit / drawdown_dollars)

    def calculate_ulcer_index(self) -> float:
        """
        Calculate Ulcer Index (measures volatility of drawdowns).

        Formula: √(Mean of squared %DD over period)

        Returns:
            Ulcer index
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        # Calculate drawdown percentage from peak
        running_max = self.df["balance"].cummax()
        drawdown_pct = ((self.df["balance"] - running_max) / running_max) * 100

        # Square each drawdown and calculate mean
        squared_dd = drawdown_pct ** 2
        ulcer = np.sqrt(squared_dd.mean())

        return abs(ulcer)

    def calculate_pain_index(self) -> float:
        """
        Calculate Pain Index (average intensity of drawdowns).

        Formula: Mean of absolute %DD over entire period

        Returns:
            Pain index
        """
        if self.df.empty or "balance" not in self.df.columns:
            return 0.0

        # Calculate drawdown percentage from peak
        running_max = self.df["balance"].cummax()
        drawdown_pct = ((self.df["balance"] - running_max) / running_max) * 100

        # Average of absolute drawdowns
        pain = abs(drawdown_pct).mean()

        return pain

    def calculate_kelly_criterion(self) -> float:
        """
        Calculate Kelly Criterion (optimal position size).

        Formula: Kelly % = (Win Rate × W/L Ratio - Loss Rate) / W/L Ratio

        Returns:
            Kelly percentage (0-100)
        """
        if self.df.empty:
            return 0.0

        win_rate = self.calculate_win_rate() / 100  # Convert to decimal
        loss_rate = 1 - win_rate
        wl_ratio = self.calculate_win_loss_ratio()

        if wl_ratio == 0:
            return 0.0

        # Kelly formula
        kelly = (win_rate * wl_ratio - loss_rate) / wl_ratio

        # Convert to percentage and cap at 100%
        kelly_pct = max(0, min(100, kelly * 100))

        return kelly_pct

    # ============================================
    # LEGACY FUNCTIONS (for compatibility)
    # ============================================

    def get_summary_metrics(self) -> Dict[str, float]:
        """
        Get summary of key metrics (legacy function).

        Returns:
            Dictionary with key metrics
        """
        return self.get_all_metrics()

    def calculate_tail_risk(self) -> Dict[str, float]:
        """
        Calculate tail risk metrics (skewness, kurtosis).

        Returns:
            Dictionary with tail risk metrics
        """
        if "returns" not in self.df.columns or len(self.df) < 4:
            return {"skewness": 0.0, "kurtosis": 0.0, "excess_kurtosis": 0.0}

        returns = self.df["returns"].values

        skew = stats.skew(returns)
        kurt = stats.kurtosis(returns)
        excess_kurt = kurt - 3  # Excess kurtosis (normal = 0)

        return {
            "skewness": skew,
            "kurtosis": kurt,
            "excess_kurtosis": excess_kurt,
            "has_fat_tails": excess_kurt > 3.0,
        }

    def get_ftmo_compliance(self) -> Dict[str, bool]:
        """
        Check FTMO rule compliance.

        Returns:
            Dictionary with compliance status
        """
        metrics = self.get_all_metrics()

        return {
            "max_drawdown_ok": metrics["ftmo_max_dd_compliant"],
            "daily_drawdown_ok": metrics["ftmo_daily_loss_compliant"],
            "overall_compliant": metrics["ftmo_max_dd_compliant"] and metrics["ftmo_daily_loss_compliant"],
            "max_drawdown_value": abs(metrics["max_drawdown_pct"]),
            "daily_drawdown_value": abs(metrics["max_daily_loss_pct"]),
        }

    def get_advanced_stats(self) -> Dict[str, any]:
        """
        Get all advanced statistics (legacy function).

        Returns:
            Complete statistics dictionary
        """
        return {
            "summary": self.get_all_metrics(),
            "tail_risk": self.calculate_tail_risk(),
            "ftmo_compliance": self.get_ftmo_compliance(),
        }
