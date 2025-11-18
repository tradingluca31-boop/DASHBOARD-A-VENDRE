"""
📊 METRICS CALCULATOR - Trading Dashboard Pro
Professional-grade trading metrics calculations
"""

from typing import List, Dict, Optional
import pandas as pd
import numpy as np
from scipy import stats


class MetricsCalculator:
    """
    Calculate institutional-grade trading metrics.

    Metrics include:
    - Performance: ROI, Total PnL, CAGR
    - Risk: Sharpe, Sortino, Calmar, Max DD
    - Trade Stats: Win Rate, Profit Factor, Expectancy
    - Advanced: VaR, CVaR, Tail Risk
    """

    def __init__(self, data: List[Dict], initial_balance: float = 10000.0):
        """
        Initialize calculator with checkpoint data.

        Args:
            data: List of checkpoint dictionaries
            initial_balance: Starting account balance
        """
        self.data = data
        self.df = pd.DataFrame(data)
        self.initial_balance = initial_balance

        # Calculate returns if not present
        if "balance" in self.df.columns:
            self.df["returns"] = self.df["balance"].pct_change().fillna(0)

    def get_summary_metrics(self) -> Dict[str, float]:
        """
        Get summary of key metrics.

        Returns:
            Dictionary with all key metrics
        """
        if self.df.empty:
            return {}

        last_row = self.df.iloc[-1]

        return {
            # Performance
            "equity": last_row.get("balance", self.initial_balance),
            "roi": last_row.get("roi", 0),
            "total_pnl": last_row.get("total_pnl", 0),
            # Trade Stats
            "total_trades": last_row.get("total_trades", 0),
            "win_rate": last_row.get("win_rate", 0),
            "profit_factor": last_row.get("profit_factor", 0),
            # Risk
            "sharpe_ratio": last_row.get("sharpe_ratio", 0),
            "max_drawdown_pct": last_row.get("max_drawdown_pct", 0),
            "max_drawdown_usd": last_row.get("max_drawdown_usd", 0),
            # Additional
            "timestep": last_row.get("timestep", 0),
            "calmar_ratio": self.calculate_calmar_ratio(),
            "sortino_ratio": self.calculate_sortino_ratio(),
        }

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
        Calculate Calmar Ratio (CAGR / Max Drawdown).

        Returns:
            Calmar ratio
        """
        if self.df.empty:
            return 0.0

        # Get max drawdown
        max_dd = abs(self.df["max_drawdown_pct"].min()) if "max_drawdown_pct" in self.df.columns else 1.0

        if max_dd == 0:
            return 0.0

        # Calculate CAGR
        cagr = self.calculate_cagr()

        return cagr / max_dd

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

        # Estimate years (assuming ~252 trading days per year)
        num_periods = len(self.df)
        years = num_periods / 252

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
        var = np.percentile(returns, (1 - confidence) * 100)

        # Average of returns below VaR
        cvar = returns[returns <= var].mean()
        return cvar * 100

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
        if self.df.empty:
            return {}

        last_row = self.df.iloc[-1]
        max_dd = abs(last_row.get("max_drawdown_pct", 0))
        daily_dd = abs(last_row.get("daily_drawdown_pct", 0))

        return {
            "max_drawdown_ok": max_dd < 10.0,
            "daily_drawdown_ok": daily_dd < 5.0,
            "overall_compliant": max_dd < 10.0 and daily_dd < 5.0,
            "max_drawdown_value": max_dd,
            "daily_drawdown_value": daily_dd,
        }

    def get_advanced_stats(self) -> Dict[str, any]:
        """
        Get all advanced statistics.

        Returns:
            Complete statistics dictionary
        """
        return {
            "summary": self.get_summary_metrics(),
            "risk_adjusted": {
                "sharpe": self.calculate_sharpe_ratio(),
                "sortino": self.calculate_sortino_ratio(),
                "calmar": self.calculate_calmar_ratio(),
                "cagr": self.calculate_cagr(),
            },
            "risk_metrics": {
                "var_95": self.calculate_var(0.95),
                "cvar_95": self.calculate_cvar(0.95),
                **self.calculate_tail_risk(),
            },
            "ftmo_compliance": self.get_ftmo_compliance(),
        }
