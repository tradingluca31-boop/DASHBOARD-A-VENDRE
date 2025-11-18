"""
📚 METRICS EXPLANATIONS - Trading Dashboard Pro
Educational tooltips for all metrics with examples
"""

METRICS_EXPLANATIONS = {
    # ============================================
    # PERFORMANCE METRICS
    # ============================================

    "roi_percent": {
        "name": "ROI (Return on Investment)",
        "description": "Mesure le rendement total de votre compte en pourcentage.",
        "formula": "ROI = ((Balance Finale - Balance Initiale) / Balance Initiale) × 100",
        "interpretation": {
            "< 0%": "❌ Perte - Compte en négatif",
            "0-5%": "🟡 Faible - Performance médiocre",
            "5-15%": "🟢 Bon - Performance correcte",
            "15-30%": "🟢 Très bon - Performance excellente",
            "> 30%": "💎 Exceptionnel - Performance institutionnelle"
        },
        "qui_utilise": "Tous les traders, hedge funds, investisseurs institutionnels",
        "exemple": "ROI de 22.8% = Votre capital a augmenté de 22.8% (10,000$ → 12,280$)"
    },

    "total_pnl": {
        "name": "Total P&L (Profit & Loss)",
        "description": "Profit ou perte total en dollars ($).",
        "formula": "P&L = Balance Finale - Balance Initiale",
        "interpretation": {
            "< 0$": "❌ Perte nette",
            "0-500$": "🟡 Profit modeste",
            "500-2000$": "🟢 Bon profit",
            "> 2000$": "💎 Excellent profit"
        },
        "qui_utilise": "Tous les traders pour mesurer le gain/perte absolu",
        "exemple": "P&L de $2,280 = Vous avez gagné 2,280$ depuis le début"
    },

    "final_balance": {
        "name": "Balance Finale",
        "description": "Capital total actuel dans votre compte.",
        "formula": "Balance Initiale + Total P&L",
        "interpretation": {
            "< Balance Initiale": "❌ Compte en perte",
            "= Balance Initiale": "🟡 Breakeven",
            "> Balance Initiale": "🟢 Compte en profit"
        },
        "qui_utilise": "Tous les traders pour suivre l'évolution du capital",
        "exemple": "Balance de $12,280 avec départ à $10,000"
    },

    "profit_factor": {
        "name": "Profit Factor",
        "description": "Ratio entre les gains totaux et les pertes totales.",
        "formula": "Profit Factor = Total Gains / Total Pertes",
        "interpretation": {
            "< 1.0": "❌ Perdant - Pertes > Gains",
            "1.0-1.3": "🟡 Faible - Juste rentable",
            "1.3-1.7": "🟢 Bon - Rentabilité solide",
            "1.7-2.5": "🟢 Très bon - Excellent",
            "> 2.5": "💎 Exceptionnel - Elite"
        },
        "qui_utilise": "Traders professionnels, prop firms (FTMO, The5ers)",
        "exemple": "Profit Factor de 1.82 = Pour chaque $1 perdu, vous gagnez $1.82"
    },

    "expectancy": {
        "name": "Expectancy (Espérance de Gain)",
        "description": "Gain moyen attendu par trade.",
        "formula": "Expectancy = (Win Rate × Avg Win) - (Loss Rate × Avg Loss)",
        "interpretation": {
            "< 0$": "❌ Négatif - Système perdant",
            "0-10$": "🟡 Faible - Juste rentable",
            "10-50$": "🟢 Bon - Système solide",
            "> 50$": "💎 Excellent - Système pro"
        },
        "qui_utilise": "Traders quantitatifs, développeurs d'algos",
        "exemple": "Expectancy de $24.8 = En moyenne, vous gagnez $24.8 par trade"
    },

    # ============================================
    # RISK METRICS
    # ============================================

    "sharpe_ratio": {
        "name": "Sharpe Ratio",
        "description": "Mesure le rendement ajusté au risque (rendement par unité de volatilité).",
        "formula": "Sharpe = (Rendement Moyen - Taux Sans Risque) / Écart-Type des Rendements",
        "interpretation": {
            "< 0": "❌ Très mauvais - Perte avec volatilité",
            "0-0.5": "🟡 Faible - Performance médiocre",
            "0.5-1.0": "🟡 Acceptable - Correct",
            "1.0-2.0": "🟢 Bon - Très bien",
            "2.0-3.0": "💎 Excellent - Institutionnel",
            "> 3.0": "🏆 Exceptionnel - Elite (rare)"
        },
        "qui_utilise": "Hedge funds, fonds d'investissement, Renaissance Technologies",
        "exemple": "Sharpe de 1.45 = Bon rendement ajusté au risque"
    },

    "sortino_ratio": {
        "name": "Sortino Ratio",
        "description": "Version améliorée du Sharpe qui ne pénalise que la volatilité négative (downside).",
        "formula": "Sortino = (Rendement Moyen - Taux Sans Risque) / Écart-Type des Rendements Négatifs",
        "interpretation": {
            "< 0": "❌ Mauvais",
            "0-1.0": "🟡 Acceptable",
            "1.0-2.0": "🟢 Bon",
            "> 2.0": "💎 Excellent"
        },
        "qui_utilise": "Bridgewater Associates, fonds long-term",
        "exemple": "Sortino de 1.67 = Excellent rendement avec faible risque de baisse"
    },

    "calmar_ratio": {
        "name": "Calmar Ratio",
        "description": "Ratio rendement/drawdown maximum. Mesure l'efficacité du système face au pire drawdown.",
        "formula": "Calmar = ROI Annualisé / Max Drawdown",
        "interpretation": {
            "< 0.5": "🟡 Faible",
            "0.5-1.0": "🟡 Acceptable",
            "1.0-3.0": "🟢 Bon",
            "3.0-5.0": "🟢 Très bon",
            "> 5.0": "💎 Excellent"
        },
        "qui_utilise": "Managed futures funds, CTA traders",
        "exemple": "Calmar de 5.7 = Excellent ratio rendement/risque de drawdown"
    },

    "max_drawdown_pct": {
        "name": "Max Drawdown (%)",
        "description": "Perte maximale depuis le pic le plus haut du compte.",
        "formula": "Max DD = ((Pic - Creux) / Pic) × 100",
        "interpretation": {
            "> 20%": "❌ Très mauvais - Risque extrême",
            "10-20%": "🟡 Élevé - À surveiller",
            "5-10%": "🟢 Acceptable - FTMO OK",
            "< 5%": "💎 Excellent - Très conservateur"
        },
        "qui_utilise": "Tous les traders, critère FTMO #1",
        "exemple": "Max DD de -7.3% = Limite FTMO (-10%) respectée ✓"
    },

    "var_95": {
        "name": "VaR 95% (Value at Risk)",
        "description": "Perte maximale probable dans 95% des cas (sur 1 jour).",
        "formula": "VaR = Percentile 5% des rendements journaliers",
        "interpretation": {
            "> -1%": "💎 Très faible risque",
            "-1% to -2%": "🟢 Faible risque",
            "-2% to -3%": "🟡 Risque modéré",
            "< -3%": "❌ Risque élevé"
        },
        "qui_utilise": "Banques d'investissement, régulateurs (Basel III)",
        "exemple": "VaR de -1.8% = 95% du temps, vous ne perdrez pas plus de 1.8% par jour"
    },

    "cvar_95": {
        "name": "CVaR 95% (Conditional VaR / Expected Shortfall)",
        "description": "Perte moyenne dans les 5% pires scénarios (tail risk).",
        "formula": "CVaR = Moyenne des pertes au-delà du VaR",
        "interpretation": {
            "> -2%": "💎 Très faible tail risk",
            "-2% to -4%": "🟢 Faible tail risk",
            "-4% to -6%": "🟡 Tail risk modéré",
            "< -6%": "❌ Tail risk élevé"
        },
        "qui_utilise": "Hedge funds, risk managers",
        "exemple": "CVaR de -2.8% = Dans les pires 5% des cas, perte moyenne de 2.8%"
    },

    # ============================================
    # TRADE ANALYSIS
    # ============================================

    "win_rate": {
        "name": "Win Rate (Taux de Réussite)",
        "description": "Pourcentage de trades gagnants.",
        "formula": "Win Rate = (Trades Gagnants / Total Trades) × 100",
        "interpretation": {
            "< 30%": "❌ Très faible",
            "30-45%": "🟡 Faible - Acceptable si bon RR",
            "45-55%": "🟢 Moyen - Bon",
            "55-70%": "🟢 Très bon",
            "> 70%": "💎 Excellent (mais vérifier le RR)"
        },
        "qui_utilise": "Tous les traders",
        "exemple": "Win Rate de 58.2% = Plus de la moitié de vos trades sont gagnants"
    },

    "avg_win": {
        "name": "Gain Moyen",
        "description": "Profit moyen par trade gagnant.",
        "formula": "Avg Win = Total Gains / Nombre de Trades Gagnants",
        "interpretation": "Plus élevé = Mieux. À comparer avec Avg Loss.",
        "qui_utilise": "Tous les traders pour analyser les performances",
        "exemple": "Avg Win de $123.2 par trade gagnant"
    },

    "avg_loss": {
        "name": "Perte Moyenne",
        "description": "Perte moyenne par trade perdant.",
        "formula": "Avg Loss = Total Pertes / Nombre de Trades Perdants",
        "interpretation": "Plus faible = Mieux. À comparer avec Avg Win.",
        "qui_utilise": "Tous les traders pour analyser le risk management",
        "exemple": "Avg Loss de $33.5 par trade perdant"
    },

    "win_loss_ratio": {
        "name": "Win/Loss Ratio (Ratio Gain/Perte)",
        "description": "Rapport entre le gain moyen et la perte moyenne.",
        "formula": "W/L Ratio = Avg Win / Avg Loss",
        "interpretation": {
            "< 1.0": "❌ Pertes > Gains (compenser avec WR > 50%)",
            "1.0-1.5": "🟡 Acceptable",
            "1.5-2.5": "🟢 Bon",
            "> 2.5": "💎 Excellent"
        },
        "qui_utilise": "Traders professionnels, prop firms",
        "exemple": "W/L Ratio de 3.68 = Vos gains sont 3.68× plus gros que vos pertes !"
    },

    "avg_trade_duration_hours": {
        "name": "Durée Moyenne des Trades",
        "description": "Temps moyen qu'un trade reste ouvert.",
        "formula": "Moyenne des durées de tous les trades",
        "interpretation": {
            "< 1h": "Scalping",
            "1-4h": "Intraday",
            "4-24h": "Day Trading",
            "> 24h": "Swing Trading"
        },
        "qui_utilise": "Tous les traders pour identifier leur style",
        "exemple": "Durée moyenne de 4.5h = Style intraday"
    },

    # ============================================
    # FTMO COMPLIANCE
    # ============================================

    "ftmo_max_dd_compliant": {
        "name": "FTMO Max Drawdown Compliance",
        "description": "Vérifie que le drawdown max ne dépasse jamais 10%.",
        "formula": "Compliant si Max DD < 10%",
        "interpretation": {
            "True": "✅ Conforme - Challenge FTMO validé",
            "False": "❌ Non conforme - Challenge FTMO échoué"
        },
        "qui_utilise": "Traders FTMO, prop firms",
        "exemple": "Max DD de -7.3% = Conforme ✓"
    },

    "ftmo_daily_loss_compliant": {
        "name": "FTMO Daily Loss Compliance",
        "description": "Vérifie qu'aucun jour ne dépasse -5% de perte.",
        "formula": "Compliant si Daily Loss < 5%",
        "interpretation": {
            "True": "✅ Conforme",
            "False": "❌ Non conforme"
        },
        "qui_utilise": "Traders FTMO, The5ers, prop firms",
        "exemple": "Max Daily Loss de -2.8% = Conforme ✓"
    },

    "trading_days": {
        "name": "Jours de Trading",
        "description": "Nombre de jours où au moins un trade a été ouvert.",
        "formula": "Compte des jours uniques avec trades",
        "interpretation": {
            "< 4 jours": "❌ FTMO: Minimum 4 jours requis",
            "≥ 4 jours": "✅ FTMO: Minimum respecté"
        },
        "qui_utilise": "FTMO Phase 1 & 2",
        "exemple": "15 jours de trading = Bien au-dessus du minimum"
    },

    # ============================================
    # ADVANCED METRICS
    # ============================================

    "recovery_factor": {
        "name": "Recovery Factor",
        "description": "Capacité à récupérer après un drawdown.",
        "formula": "Recovery Factor = Net Profit / Max Drawdown (en $)",
        "interpretation": {
            "< 1.0": "🟡 Récupération difficile",
            "1.0-3.0": "🟢 Bon",
            "3.0-10.0": "🟢 Très bon",
            "> 10.0": "💎 Excellent"
        },
        "qui_utilise": "Traders professionnels",
        "exemple": "Recovery Factor de 5.2 = Vous récupérez facilement des drawdowns"
    },

    "ulcer_index": {
        "name": "Ulcer Index",
        "description": "Mesure le stress/la douleur causée par les drawdowns (volatilité des DD).",
        "formula": "Ulcer Index = √(Moyenne des carrés des %DD sur période)",
        "interpretation": {
            "< 1.0": "💎 Très faible stress",
            "1.0-3.0": "🟢 Faible stress",
            "3.0-5.0": "🟡 Stress modéré",
            "> 5.0": "❌ Stress élevé"
        },
        "qui_utilise": "Développé par Peter Martin (1987), utilisé par les fonds",
        "exemple": "Ulcer Index de 2.1 = Drawdowns peu stressants"
    },

    "pain_index": {
        "name": "Pain Index",
        "description": "Intensité moyenne de la douleur psychologique des drawdowns.",
        "formula": "Pain Index = Moyenne des %DD absolus sur toute la période",
        "interpretation": {
            "< 1.0": "💎 Très faible douleur",
            "1.0-3.0": "🟢 Faible douleur",
            "3.0-5.0": "🟡 Douleur modérée",
            "> 5.0": "❌ Douleur élevée"
        },
        "qui_utilise": "Traders quantitatifs",
        "exemple": "Pain Index de 1.8 = Faible souffrance psychologique"
    },

    "kelly_criterion": {
        "name": "Kelly Criterion",
        "description": "Taille de position optimale pour maximiser la croissance du capital.",
        "formula": "Kelly % = (Win Rate × W/L Ratio - Loss Rate) / W/L Ratio",
        "interpretation": {
            "< 0%": "❌ Système non rentable",
            "0-5%": "🟡 Faible edge - Positions petites",
            "5-15%": "🟢 Bon edge - Positions standard",
            "15-25%": "💎 Fort edge - Positions grosses",
            "> 25%": "⚠️ Attention - Réduire de moitié (Half Kelly)"
        },
        "qui_utilise": "Ed Thorp (BlackJack), Renaissance Technologies, traders quants",
        "exemple": "Kelly de 12% = Utilisez 12% de votre capital par trade (ou 6% en Half Kelly)"
    },
}


def get_metric_explanation(metric_key: str) -> dict:
    """Get explanation for a specific metric"""
    return METRICS_EXPLANATIONS.get(metric_key, {
        "name": metric_key,
        "description": "Métrique de trading",
        "formula": "N/A",
        "interpretation": "N/A",
        "qui_utilise": "Traders",
        "exemple": "N/A"
    })


def format_metric_tooltip(metric_key: str) -> str:
    """Format metric explanation as HTML tooltip"""
    exp = get_metric_explanation(metric_key)

    html = f"""
    <div class='metric-tooltip'>
        <h5>{exp['name']}</h5>
        <p><strong>📋 Description:</strong> {exp['description']}</p>
        <p><strong>🧮 Formule:</strong> {exp['formula']}</p>
        <p><strong>👥 Qui l'utilise:</strong> {exp['qui_utilise']}</p>
        <p><strong>💡 Exemple:</strong> {exp['exemple']}</p>
        <p><strong>📊 Interprétation:</strong></p>
        <ul>
    """

    if isinstance(exp['interpretation'], dict):
        for range_val, meaning in exp['interpretation'].items():
            html += f"<li><strong>{range_val}:</strong> {meaning}</li>"
    else:
        html += f"<li>{exp['interpretation']}</li>"

    html += """
        </ul>
    </div>
    """

    return html
