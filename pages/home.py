"""
🏠 PAGE D'ACCUEIL - Trading Dashboard Pro V2.5 ULTRA-MODERNE
Design 2025 : Glassmorphism, Animations, Typographie Moderne
100% Français | Inspired by Linear, Vercel, Stripe
"""

from typing import Optional, List, Dict
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

# ============================================
# 🎨 PALETTE MODERNE
# ============================================

COLORS = {
    'cyan': '#00d9ff',
    'orange': '#ff6b35',
    'violet': '#7b68ee',
    'blue': '#4a90e2',
    'green': '#28a745',
    'yellow': '#ffc107',
    'pink': '#ff6b9d',
    'red': '#dc3545',
}

# ============================================
# 📐 LAYOUT PRINCIPAL
# ============================================


def layout():
    """Page d'accueil moderne avec glassmorphism"""
    return dbc.Container(
        fluid=True,
        className="px-4 py-5",
        children=[
            # ============================================
            # 🎯 EN-TÊTE AVEC GRADIENT
            # ============================================
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H1(
                                        "📊 Tableau de Bord Trading Pro",
                                        className="mb-3",
                                        style={'textAlign': 'center'},
                                    ),
                                    html.P(
                                        "Analyse institutionnelle • 30+ Métriques Hedge Fund • IA-Powered",
                                        className="lead text-muted text-center mb-5",
                                        style={'fontSize': '1.2rem', 'fontWeight': '500'},
                                    ),
                                ],
                            ),
                        ],
                        width=12,
                    ),
                ],
            ),
            # ============================================
            # 📤 UPLOAD SECTION GLASSMORPHISM
            # ============================================
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.Div(
                                            [
                                                html.I(className="fas fa-cloud-upload-alt fa-2x me-3", style={'color': COLORS['cyan']}),
                                                html.Span("Télécharger vos Données", style={'fontSize': '1.4rem', 'fontWeight': '800'}),
                                            ],
                                            className="d-flex align-items-center justify-content-center py-2",
                                        ),
                                    ),
                                    dbc.CardBody(
                                        [
                                            dcc.Upload(
                                                id="upload-data",
                                                children=html.Div(
                                                    [
                                                        html.I(
                                                            className="fas fa-cloud-upload-alt mb-4",
                                                            style={'fontSize': '5rem', 'color': COLORS['cyan'], 'opacity': '0.9'},
                                                        ),
                                                        html.H3(
                                                            "Glissez-déposez vos fichiers ici",
                                                            className="mb-3",
                                                            style={'fontWeight': '700', 'fontSize': '1.8rem'},
                                                        ),
                                                        html.P(
                                                            "ou cliquez pour sélectionner",
                                                            className="text-muted mb-4",
                                                            style={'fontSize': '1.15rem'},
                                                        ),
                                                        html.Div(
                                                            [
                                                                dbc.Badge("ZIP", pill=True, color="info", className="me-3 px-4 py-2", style={'fontSize': '1.1rem'}),
                                                                dbc.Badge("JSON", pill=True, color="success", className="me-3 px-4 py-2", style={'fontSize': '1.1rem'}),
                                                                dbc.Badge("CSV", pill=True, color="warning", className="me-3 px-4 py-2", style={'fontSize': '1.1rem'}),
                                                                dbc.Badge("XLSX", pill=True, color="danger", className="px-4 py-2", style={'fontSize': '1.1rem'}),
                                                            ],
                                                            className="d-flex justify-content-center flex-wrap mt-4",
                                                        ),
                                                    ],
                                                    className="text-center py-4",
                                                ),
                                                multiple=False,
                                            ),
                                        ],
                                        className="p-5",
                                    ),
                                ],
                                className="mb-5 premium-border",
                            ),
                        ],
                        lg=10,
                        xl=8,
                        className="mx-auto",
                    ),
                ],
            ),
            # ============================================
            # 🎯 CONTENU DYNAMIQUE
            # ============================================
            html.Div(id="dashboard-content", className="mt-5"),
            # Storage
            dcc.Store(id="stored-data"),
        ],
    )


# ============================================
# 💎 HERO CARD (Top 3 métriques)
# ============================================


def create_hero_metric(icon, label, value, subtitle, color, glow_class):
    """Carte hero avec glassmorphism et glow"""
    return dbc.Col(
        [
            html.Div(
                [
                    html.I(className=f"{icon} fa-3x mb-4", style={'color': color, 'opacity': '0.9'}),
                    html.H2(
                        value,
                        className=f"mb-3 text-gradient-{glow_class}",
                        style={'fontSize': '3.8rem', 'fontWeight': '900'},
                    ),
                    html.P(
                        label,
                        className="text-muted mb-2",
                        style={'fontSize': '0.95rem', 'fontWeight': '700', 'textTransform': 'uppercase', 'letterSpacing': '0.15em'},
                    ),
                    html.P(
                        subtitle,
                        className="mb-0",
                        style={'fontSize': '1.05rem', 'opacity': '0.75', 'fontWeight': '500'},
                    ),
                ],
                className=f"hero-card hero-card-{glow_class} text-center",
            ),
        ],
        lg=4,
        md=6,
        className="mb-4",
    )


# ============================================
# 📊 CARTE MÉTRIQUE STANDARD
# ============================================


def create_metric_card(label, value, icon, color, description=""):
    """Carte métrique glassmorphism avec hover"""
    return dbc.Col(
        [
            html.Div(
                [
                    html.I(className=icon, style={'color': color, 'fontSize': '2rem', 'opacity': '0.85', 'marginBottom': '1rem'}),
                    html.H4(
                        value,
                        className="mb-2",
                        style={'fontSize': '2.2rem', 'fontWeight': '800', 'color': color},
                    ),
                    html.P(
                        label,
                        className="text-muted mb-1",
                        style={'fontSize': '0.95rem', 'fontWeight': '600'},
                    ),
                    html.P(
                        description,
                        className="mb-0",
                        style={'fontSize': '0.8rem', 'opacity': '0.6'},
                    ) if description else None,
                ],
                className="metric-card text-center",
                style={'--accent-color': color},
            ),
        ],
        lg=3,
        md=6,
        sm=12,
        className="mb-4",
    )


# ============================================
# 📈 GRAPHIQUE EQUITY MODERNE
# ============================================


def create_modern_equity_chart(df: pd.DataFrame) -> go.Figure:
    """Equity curve avec gradient et glassmorphism"""
    fig = go.Figure()

    balance_col = 'balance' if 'balance' in df.columns else 'total_reward'

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[balance_col],
            mode='lines',
            name='Balance',
            line=dict(color=COLORS['cyan'], width=4),
            fill='tozeroy',
            fillcolor='rgba(0, 217, 255, 0.15)',
            hovertemplate='<b>Step</b>: %{x}<br><b>Balance</b>: $%{y:,.2f}<extra></extra>',
        )
    )

    fig.update_layout(
        title={
            'text': '<b>📈 Évolution de la Balance</b>',
            'font': {'size': 28, 'family': 'Inter', 'color': '#fff'},
            'x': 0.5,
            'xanchor': 'center',
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(22, 27, 46, 0.4)',
        font=dict(family="Inter", color='#fff', size=14),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="rgba(22, 27, 46, 0.95)",
            font_size=15,
            font_family="Inter",
            bordercolor=COLORS['cyan'],
        ),
        xaxis=dict(
            title='<b>Checkpoints</b>',
            gridcolor='rgba(255, 255, 255, 0.06)',
            showgrid=True,
            zeroline=False,
        ),
        yaxis=dict(
            title='<b>Balance ($)</b>',
            gridcolor='rgba(255, 255, 255, 0.06)',
            showgrid=True,
            zeroline=False,
        ),
        margin=dict(l=60, r=40, t=100, b=60),
        height=500,
    )

    return fig


# ============================================
# 🍩 DONUT WIN/LOSS
# ============================================


def create_winloss_donut(metrics: Dict) -> go.Figure:
    """Donut chart moderne"""
    winning = metrics.get("winning_trades", 0)
    losing = metrics.get("losing_trades", 0)

    fig = go.Figure(
        data=[
            go.Pie(
                labels=['Trades Gagnants', 'Trades Perdants'],
                values=[winning, losing],
                hole=0.65,
                marker=dict(
                    colors=[COLORS['green'], COLORS['red']],
                    line=dict(color='rgba(255,255,255,0.1)', width=3),
                ),
                textfont=dict(size=16, family='Inter', color='#fff'),
                hovertemplate='<b>%{label}</b><br>%{value} trades<br>%{percent}<extra></extra>',
            )
        ]
    )

    total_trades = winning + losing
    win_rate = (winning / total_trades * 100) if total_trades > 0 else 0

    fig.add_annotation(
        text=f"<b style='font-size:36px'>{win_rate:.1f}%</b><br><span style='font-size:16px;opacity:0.7'>Win Rate</span>",
        x=0.5,
        y=0.5,
        font=dict(size=18, family='Inter', color='#fff'),
        showarrow=False,
    )

    fig.update_layout(
        title={
            'text': '<b>🎯 Répartition des Trades</b>',
            'font': {'size': 26, 'family': 'Inter', 'color': '#fff'},
            'x': 0.5,
            'xanchor': 'center',
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", color='#fff'),
        margin=dict(l=40, r=40, t=90, b=60),
        height=450,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="center",
            x=0.5,
            font=dict(size=14),
        ),
    )

    return fig


# ============================================
# 🎯 DASHBOARD COMPLET
# ============================================


def create_dashboard_content(metrics: Dict, df: pd.DataFrame):
    """Contenu complet du dashboard moderne"""

    return html.Div(
        [
            # ============================================
            # 🌟 HERO METRICS (Top 3)
            # ============================================
            dbc.Row(
                [
                    create_hero_metric(
                        icon="fas fa-chart-line",
                        label="Rendement Total",
                        value=f"{metrics.get('roi_percent', 0):+.2f}%",
                        subtitle=f"P&L: ${metrics.get('total_pnl', 0):,.2f}",
                        color=COLORS['cyan'],
                        glow_class="cyan",
                    ),
                    create_hero_metric(
                        icon="fas fa-trophy",
                        label="Sharpe Ratio",
                        value=f"{metrics.get('sharpe_ratio', 0):.2f}",
                        subtitle="Performance / Risque",
                        color=COLORS['orange'],
                        glow_class="orange",
                    ),
                    create_hero_metric(
                        icon="fas fa-shield-alt",
                        label="Max Drawdown",
                        value=f"{abs(metrics.get('max_drawdown_pct', 0)):.2f}%",
                        subtitle="Perte Maximale",
                        color=COLORS['violet'],
                        glow_class="violet",
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # 📊 GRAPHIQUES PRINCIPAUX
            # ============================================
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    dcc.Graph(figure=create_modern_equity_chart(df), config={'displayModeBar': False}),
                                    className="p-4",
                                ),
                                className="glass-effect",
                            ),
                        ],
                        lg=8,
                        className="mb-4",
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    dcc.Graph(figure=create_winloss_donut(metrics), config={'displayModeBar': False}),
                                    className="p-4",
                                ),
                                className="glass-effect",
                            ),
                        ],
                        lg=4,
                        className="mb-4",
                    ),
                ],
            ),
            # ============================================
            # 💼 PERFORMANCE
            # ============================================
            html.Div(
                [
                    html.H3(
                        [html.I(className="fas fa-chart-bar me-3"), "Performance"],
                        className="mb-4 text-gradient-cyan",
                        style={'fontSize': '2.2rem', 'fontWeight': '900'},
                    ),
                    dbc.Row(
                        [
                            create_metric_card("Profit Factor", f"{metrics.get('profit_factor', 0):.2f}", "fas fa-balance-scale", COLORS['cyan'], "Gains / Pertes"),
                            create_metric_card("Espérance", f"${metrics.get('expectancy', 0):.2f}", "fas fa-dollar-sign", COLORS['green'], "Profit par trade"),
                            create_metric_card("CAGR", f"{metrics.get('cagr', 0):.2f}%", "fas fa-percent", COLORS['blue'], "Croissance annuelle"),
                            create_metric_card("Balance Finale", f"${metrics.get('final_balance', 0):,.0f}", "fas fa-wallet", COLORS['orange'], "Solde actuel"),
                        ],
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # 🛡️ GESTION DU RISQUE
            # ============================================
            html.Div(
                [
                    html.H3(
                        [html.I(className="fas fa-shield-alt me-3"), "Gestion du Risque"],
                        className="mb-4 text-gradient-orange",
                        style={'fontSize': '2.2rem', 'fontWeight': '900'},
                    ),
                    dbc.Row(
                        [
                            create_metric_card("Sortino Ratio", f"{metrics.get('sortino_ratio', 0):.2f}", "fas fa-chart-area", COLORS['violet'], "Risque baissier"),
                            create_metric_card("Calmar Ratio", f"{metrics.get('calmar_ratio', 0):.2f}", "fas fa-signal", COLORS['pink'], "CAGR / Max DD"),
                            create_metric_card("VaR 95%", f"{metrics.get('var_95', 0):.2f}%", "fas fa-exclamation-triangle", COLORS['yellow'], "Value at Risk"),
                            create_metric_card("CVaR 95%", f"{metrics.get('cvar_95', 0):.2f}%", "fas fa-shield-virus", COLORS['red'], "Risque de queue"),
                        ],
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # 📈 STATISTIQUES TRADING
            # ============================================
            html.Div(
                [
                    html.H3(
                        [html.I(className="fas fa-exchange-alt me-3"), "Statistiques de Trading"],
                        className="mb-4 text-gradient-violet",
                        style={'fontSize': '2.2rem', 'fontWeight': '900'},
                    ),
                    dbc.Row(
                        [
                            create_metric_card("Total Trades", f"{metrics.get('total_trades', 0)}", "fas fa-list-ol", COLORS['cyan'], "Positions totales"),
                            create_metric_card("Win Rate", f"{metrics.get('win_rate', 0):.1f}%", "fas fa-percentage", COLORS['green'], "Taux de réussite"),
                            create_metric_card("Gain Moyen", f"${metrics.get('avg_win', 0):,.2f}", "fas fa-arrow-up", COLORS['green'], "Par trade gagnant"),
                            create_metric_card("Perte Moyenne", f"${abs(metrics.get('avg_loss', 0)):,.2f}", "fas fa-arrow-down", COLORS['red'], "Par trade perdant"),
                            create_metric_card("Meilleur Trade", f"${metrics.get('best_trade', 0):,.2f}", "fas fa-star", COLORS['yellow'], "Plus gros gain"),
                            create_metric_card("Pire Trade", f"${abs(metrics.get('worst_trade', 0)):,.2f}", "fas fa-skull", COLORS['red'], "Plus grosse perte"),
                            create_metric_card("Ratio W/L", f"{metrics.get('win_loss_ratio', 0):.2f}", "fas fa-divide", COLORS['blue'], "Gain / Perte"),
                            create_metric_card("Durée Moy", f"{metrics.get('avg_trade_duration_hours', 0):.1f}h", "fas fa-clock", COLORS['violet'], "Par position"),
                        ],
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # 💎 MÉTRIQUES AVANCÉES
            # ============================================
            html.Div(
                [
                    html.H3(
                        [html.I(className="fas fa-gem me-3"), "Métriques Avancées"],
                        className="mb-4",
                        style={
                            'fontSize': '2.2rem',
                            'fontWeight': '900',
                            'background': 'linear-gradient(135deg, #00d9ff, #ff6b35, #7b68ee)',
                            '-webkit-background-clip': 'text',
                            '-webkit-text-fill-color': 'transparent',
                            'backgroundClip': 'text',
                        },
                    ),
                    dbc.Row(
                        [
                            create_metric_card("Recovery Factor", f"{metrics.get('recovery_factor', 0):.2f}", "fas fa-heartbeat", COLORS['green'], "Profit / Max DD"),
                            create_metric_card("Ulcer Index", f"{metrics.get('ulcer_index', 0):.2f}", "fas fa-wave-square", COLORS['orange'], "Volatilité DD"),
                            create_metric_card("Pain Index", f"{metrics.get('pain_index', 0):.2f}", "fas fa-thermometer-half", COLORS['pink'], "Intensité DD"),
                            create_metric_card("Kelly Criterion", f"{metrics.get('kelly_criterion', 0):.1f}%", "fas fa-bullseye", COLORS['cyan'], "Position optimale"),
                        ],
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # ✅ FTMO COMPLIANCE
            # ============================================
            html.Div(
                [
                    html.H3(
                        [html.I(className="fas fa-check-circle me-3"), "Conformité FTMO"],
                        className="mb-4",
                        style={
                            'fontSize': '2.2rem',
                            'fontWeight': '900',
                            'background': 'linear-gradient(135deg, #28a745, #20c997)',
                            '-webkit-background-clip': 'text',
                            '-webkit-text-fill-color': 'transparent',
                            'backgroundClip': 'text',
                        },
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Alert(
                                        [
                                            html.I(className="fas fa-check-circle fa-3x mb-3" if metrics.get('ftmo_max_dd_compliant', False) else "fas fa-times-circle fa-3x mb-3"),
                                            html.H4("Max Drawdown < 10%", className="mb-3 fw-bold"),
                                            html.H5(f"{abs(metrics.get('max_drawdown_pct', 0)):.2f}%", className="mb-2", style={'fontSize': '2.5rem', 'fontWeight': '900'}),
                                            html.P("Limite FTMO", className="mb-0", style={'opacity': '0.8'}),
                                        ],
                                        color="success" if metrics.get('ftmo_max_dd_compliant', False) else "danger",
                                        className="text-center glass-effect py-4",
                                    ),
                                ],
                                lg=4,
                                md=6,
                                className="mb-4",
                            ),
                            dbc.Col(
                                [
                                    dbc.Alert(
                                        [
                                            html.I(className="fas fa-calendar-day fa-3x mb-3" if metrics.get('ftmo_daily_loss_compliant', False) else "fas fa-exclamation-circle fa-3x mb-3"),
                                            html.H4("Perte Journalière < 5%", className="mb-3 fw-bold"),
                                            html.H5(f"{abs(metrics.get('max_daily_loss_pct', 0)):.2f}%", className="mb-2", style={'fontSize': '2.5rem', 'fontWeight': '900'}),
                                            html.P("Limite FTMO", className="mb-0", style={'opacity': '0.8'}),
                                        ],
                                        color="success" if metrics.get('ftmo_daily_loss_compliant', False) else "danger",
                                        className="text-center glass-effect py-4",
                                    ),
                                ],
                                lg=4,
                                md=6,
                                className="mb-4",
                            ),
                            dbc.Col(
                                [
                                    dbc.Alert(
                                        [
                                            html.I(className="fas fa-calendar-check fa-3x mb-3"),
                                            html.H4("Jours de Trading", className="mb-3 fw-bold"),
                                            html.H5(f"{metrics.get('trading_days', 0)}", className="mb-2", style={'fontSize': '2.5rem', 'fontWeight': '900'}),
                                            html.P("Min: 4 jours", className="mb-0", style={'opacity': '0.8'}),
                                        ],
                                        color="info",
                                        className="text-center glass-effect py-4",
                                    ),
                                ],
                                lg=4,
                                md=12,
                                className="mb-4",
                            ),
                        ],
                    ),
                ],
                className="mb-5",
            ),
            # ============================================
            # 📥 EXPORT
            # ============================================
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button(
                                [html.I(className="fas fa-download me-3"), "Télécharger les Données (CSV)"],
                                id="download-csv-btn",
                                size="lg",
                                className="w-100 premium-border",
                                style={
                                    'background': f'linear-gradient(135deg, {COLORS["cyan"]}, {COLORS["violet"]})',
                                    'border': 'none',
                                    'fontSize': '1.2rem',
                                    'fontWeight': '800',
                                    'padding': '1.2rem',
                                    'borderRadius': '16px',
                                },
                            ),
                            dcc.Download(id="download-csv"),
                        ],
                        lg=6,
                        xl=5,
                        className="mx-auto",
                    ),
                ],
                className="text-center mt-4",
            ),
        ]
    )


# ============================================
# 🔄 CALLBACKS
# ============================================


@callback(
    [Output("dashboard-content", "children"), Output("stored-data", "data")],
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
)
def update_dashboard(contents, filename):
    """Callback principal"""
    if contents is None:
        return html.Div(
            [
                dbc.Alert(
                    [
                        html.I(className="fas fa-info-circle fa-3x mb-4"),
                        html.H3("Aucune donnée chargée", className="mb-3 fw-bold"),
                        html.P(
                            "Téléchargez un fichier pour commencer l'analyse de vos performances trading.",
                            className="mb-0",
                            style={'fontSize': '1.1rem'},
                        ),
                    ],
                    color="info",
                    className="text-center glass-effect mt-5 py-5",
                ),
            ],
        ), None

    from utils.data_loader import DataLoader
    from utils.metrics import MetricsCalculator

    try:
        loader = DataLoader()
        data = loader.parse_upload(contents, filename)

        if data is None:
            raise ValueError("Échec du parsing. Vérifiez le format du fichier.")

        df = pd.DataFrame(data)
        calculator = MetricsCalculator(data)
        metrics = calculator.get_all_metrics()

        content = create_dashboard_content(metrics, df)

        return content, data

    except Exception as e:
        return (
            dbc.Alert(
                [
                    html.I(className="fas fa-exclamation-triangle fa-3x mb-4"),
                    html.H3("Erreur de Chargement", className="mb-3 fw-bold"),
                    html.P(f"Détails : {str(e)}", className="mb-0", style={'fontSize': '1rem'}),
                ],
                color="danger",
                className="text-center glass-effect mt-5 py-5",
            ),
            None,
        )


@callback(
    Output("download-csv", "data"),
    Input("download-csv-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True,
)
def download_csv(n_clicks, data):
    """Export CSV"""
    if data is None:
        return None

    df = pd.DataFrame(data)
    return dcc.send_data_frame(df.to_csv, "trading_analytics.csv", index=False)
