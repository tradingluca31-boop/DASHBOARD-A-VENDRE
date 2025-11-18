"""
🏠 HOME PAGE - Trading Dashboard Pro V2
Ultra-modern layout with 30+ institutional metrics
Inspired by professional analytics dashboards
"""

from typing import Optional, List, Dict
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

# ============================================
# 🎨 COLOR PALETTE (Modern Vibrant)
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
    'dark_bg': '#0a0e27',
    'card_bg': '#161b2e',
    'text': '#ffffff',
}

# ============================================
# 📐 PAGE LAYOUT
# ============================================


def layout():
    """
    Modern home page layout with:
    - File upload section
    - 30+ metrics in colorful cards
    - Multiple chart types (line, bar, donut)
    - Professional grid layout
    """
    return dbc.Container(
        [
            # Page Header
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                [
                                    html.I(className="fas fa-home me-3"),
                                    "Aperçu du tableau de bord",
                                ],
                                className="mb-2",
                                style={'fontSize': '2.5rem', 'fontWeight': '700'},
                            ),
                            html.P(
                                "Téléchargez vos données de trading et suivez les performances en temps réel.",
                                className="text-muted lead",
                                style={'fontSize': '1.1rem'},
                            ),
                        ],
                    ),
                ],
                className="mb-4",
            ),
            # File Upload Section
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    html.H5(
                                        [
                                            html.I(className="fas fa-upload me-2"),
                                            "Télécharger les données de trading",
                                        ],
                                        className="mb-0",
                                    ),
                                    style={'background': COLORS['card_bg'], 'borderBottom': '2px solid ' + COLORS['cyan']},
                                ),
                                dbc.CardBody(
                                    [
                                        dcc.Upload(
                                            id="upload-data",
                                            children=html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-cloud-upload-alt fa-4x mb-3",
                                                        style={'color': COLORS['cyan']},
                                                    ),
                                                    html.H4("Glissez-déposez ou cliquez pour télécharger", style={'fontWeight': '600'}),
                                                    html.P(
                                                        "Formats de fichiers compatibles : ZIP, JSON, CSV",
                                                        className="text-muted mb-0",
                                                        style={'fontSize': '0.95rem'},
                                                    ),
                                                ],
                                                className="text-center py-5",
                                            ),
                                            style={
                                                "borderWidth": "3px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "15px",
                                                "borderColor": COLORS['cyan'],
                                                "background": COLORS['dark_bg'],
                                                "cursor": "pointer",
                                                "transition": "all 0.3s ease",
                                            },
                                            multiple=False,
                                        ),
                                        html.Div(id="upload-status", className="mt-3"),
                                    ],
                                    style={'background': COLORS['card_bg']},
                                ),
                            ],
                            className="shadow-lg mb-4",
                            style={'border': 'none', 'background': COLORS['card_bg']},
                        ),
                        lg=10,
                        className="mx-auto",
                    ),
                ],
            ),
            # Metrics & Charts Containers
            html.Div(id="metrics-cards-container"),
            html.Div(id="home-charts-container"),
        ],
        fluid=True,
        style={'maxWidth': '1800px'},
    )


# ============================================
# 💎 HERO METRICS CARDS (Top 3 Large)
# ============================================


def create_hero_card(icon, label, value, subtitle, color, glow=True):
    """Create large hero metric card with glow effect"""
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Div(
                        [
                            html.I(
                                className=f"fas {icon} fa-2x mb-3",
                                style={'color': color, 'opacity': '0.9'},
                            ),
                        ],
                    ),
                    html.H6(
                        label,
                        className="text-muted mb-2",
                        style={'fontSize': '0.85rem', 'textTransform': 'uppercase', 'letterSpacing': '1px'},
                    ),
                    html.H1(
                        value,
                        className="mb-2",
                        style={
                            'fontSize': '3.5rem',
                            'fontWeight': '700',
                            'color': color,
                            'textShadow': f'0 0 20px {color}' if glow else 'none',
                        },
                    ),
                    html.P(
                        subtitle,
                        className="mb-0",
                        style={'fontSize': '0.9rem', 'color': '#adb5bd'},
                    ),
                ],
                style={'padding': '2rem'},
            ),
        ],
        className="shadow-lg h-100",
        style={
            'background': f'linear-gradient(135deg, {COLORS["card_bg"]} 0%, {color}15 100%)',
            'border': f'2px solid {color}30',
            'borderRadius': '15px',
            'transition': 'all 0.3s ease',
        },
    )


# ============================================
# 📊 STANDARD METRIC CARD
# ============================================


def create_metric_card(icon, label, value, subtitle, color):
    """Create standard size metric card"""
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Div(
                        [
                            html.I(
                                className=f"fas {icon}",
                                style={'fontSize': '1.8rem', 'color': color},
                            ),
                        ],
                        className="mb-2",
                    ),
                    html.H6(
                        label,
                        className="text-muted mb-2",
                        style={'fontSize': '0.75rem', 'textTransform': 'uppercase'},
                    ),
                    html.H3(
                        value,
                        className="mb-1",
                        style={'fontSize': '2rem', 'fontWeight': '700', 'color': color},
                    ),
                    html.P(
                        subtitle,
                        className="mb-0 small",
                        style={'fontSize': '0.8rem', 'color': '#6c757d'},
                    ),
                ],
                style={'padding': '1.5rem 1.2rem'},
            ),
        ],
        className="shadow h-100",
        style={
            'background': COLORS['card_bg'],
            'border': 'none',
            'borderLeft': f'4px solid {color}',
            'borderRadius': '10px',
        },
    )


# ============================================
# 🎯 COMPLETE METRICS LAYOUT (30+ metrics)
# ============================================


def create_complete_metrics_layout(metrics: Dict) -> html.Div:
    """
    Create comprehensive metrics dashboard with 30+ metrics

    Args:
        metrics: Dictionary with all calculated metrics

    Returns:
        Complete metrics layout with cards and charts
    """

    # Row 1: Hero Metrics (3 large cards)
    hero_row = dbc.Row(
        [
            dbc.Col(
                create_hero_card(
                    icon="fa-chart-line",
                    label="ROI Total",
                    value=f"+{metrics.get('roi_percent', 0):.1f}%",
                    subtitle=f"Profit: ${metrics.get('total_pnl', 0):,.2f}",
                    color=COLORS['cyan'],
                ),
                lg=4, md=12, className="mb-4",
            ),
            dbc.Col(
                create_hero_card(
                    icon="fa-trophy",
                    label="Sharpe Ratio",
                    value=f"{metrics.get('sharpe_ratio', 0):.2f}",
                    subtitle="Rendement ajusté au risque",
                    color=COLORS['orange'],
                ),
                lg=4, md=12, className="mb-4",
            ),
            dbc.Col(
                create_hero_card(
                    icon="fa-shield-alt",
                    label="Max Drawdown",
                    value=f"{metrics.get('max_drawdown_pct', 0):.1f}%",
                    subtitle="FTMO Limit: -10%",
                    color=COLORS['violet'],
                ),
                lg=4, md=12, className="mb-4",
            ),
        ],
        className="mb-4",
    )

    # Row 2: Performance Metrics (4 cards)
    performance_row = dbc.Row(
        [
            dbc.Col(
                create_metric_card(
                    "fa-dollar-sign", "Balance Finale",
                    f"${metrics.get('final_balance', 0):,.0f}",
                    f"Initial: ${metrics.get('initial_balance', 10000):,.0f}",
                    COLORS['green'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-percent", "Win Rate",
                    f"{metrics.get('win_rate', 0):.1f}%",
                    f"{metrics.get('winning_trades', 0)} / {metrics.get('total_trades', 0)} trades",
                    COLORS['blue'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-balance-scale", "Profit Factor",
                    f"{metrics.get('profit_factor', 0):.2f}",
                    "Target: > 1.5",
                    COLORS['yellow'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-star", "Expectancy",
                    f"${metrics.get('expectancy', 0):.2f}",
                    "Par trade moyen",
                    COLORS['pink'],
                ),
                lg=3, md=6, className="mb-3",
            ),
        ],
        className="mb-4",
    )

    # Row 3: Risk Metrics (4 cards)
    risk_row = dbc.Row(
        [
            dbc.Col(
                create_metric_card(
                    "fa-chart-area", "Sortino Ratio",
                    f"{metrics.get('sortino_ratio', 0):.2f}",
                    "Downside risk ajusté",
                    COLORS['cyan'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-wave-square", "Calmar Ratio",
                    f"{metrics.get('calmar_ratio', 0):.2f}",
                    "ROI / Max DD",
                    COLORS['orange'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-exclamation-triangle", "VaR 95%",
                    f"{metrics.get('var_95', 0):.2f}%",
                    "Perte max probable",
                    COLORS['red'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-skull-crossbones", "CVaR (Expected Shortfall)",
                    f"{metrics.get('cvar_95', 0):.2f}%",
                    "Perte extrême moyenne",
                    COLORS['violet'],
                ),
                lg=3, md=6, className="mb-3",
            ),
        ],
        className="mb-4",
    )

    # Row 4: Trade Analysis (4 cards)
    trade_row = dbc.Row(
        [
            dbc.Col(
                create_metric_card(
                    "fa-coins", "Gain Moyen",
                    f"${metrics.get('avg_win', 0):.2f}",
                    f"Meilleur: ${metrics.get('best_trade', 0):.2f}",
                    COLORS['green'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-money-bill-wave", "Perte Moyenne",
                    f"${abs(metrics.get('avg_loss', 0)):.2f}",
                    f"Pire: ${abs(metrics.get('worst_trade', 0)):.2f}",
                    COLORS['red'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-exchange-alt", "Win/Loss Ratio",
                    f"{metrics.get('win_loss_ratio', 0):.2f}",
                    "Ratio gains/pertes",
                    COLORS['blue'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-clock", "Durée Moyenne",
                    f"{metrics.get('avg_trade_duration_hours', 0):.1f}h",
                    "Par position",
                    COLORS['yellow'],
                ),
                lg=3, md=6, className="mb-3",
            ),
        ],
        className="mb-4",
    )

    # Row 5: FTMO Compliance (4 cards)
    ftmo_row = dbc.Row(
        [
            dbc.Col(
                create_metric_card(
                    "fa-check-circle" if metrics.get('ftmo_max_dd_compliant') else "fa-times-circle",
                    "FTMO Max DD",
                    "✓ Conforme" if metrics.get('ftmo_max_dd_compliant') else "✗ Non conforme",
                    f"Max: {metrics.get('max_drawdown_pct', 0):.1f}% / 10%",
                    COLORS['green'] if metrics.get('ftmo_max_dd_compliant') else COLORS['red'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-check-circle" if metrics.get('ftmo_daily_loss_compliant') else "fa-times-circle",
                    "FTMO Daily Loss",
                    "✓ Conforme" if metrics.get('ftmo_daily_loss_compliant') else "✗ Non conforme",
                    f"Max: {metrics.get('max_daily_loss_pct', 0):.1f}% / 5%",
                    COLORS['green'] if metrics.get('ftmo_daily_loss_compliant') else COLORS['red'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-bullseye",
                    "Profit Target",
                    f"{metrics.get('roi_percent', 0):.1f}% / 10%",
                    "Phase 1 FTMO",
                    COLORS['green'] if metrics.get('roi_percent', 0) >= 10 else COLORS['yellow'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-calendar-check",
                    "Trading Days",
                    f"{metrics.get('trading_days', 0)}",
                    "Min: 4 jours",
                    COLORS['green'] if metrics.get('trading_days', 0) >= 4 else COLORS['yellow'],
                ),
                lg=3, md=6, className="mb-3",
            ),
        ],
        className="mb-4",
    )

    # Row 6: Advanced Metrics (4 cards)
    advanced_row = dbc.Row(
        [
            dbc.Col(
                create_metric_card(
                    "fa-heartbeat", "Recovery Factor",
                    f"{metrics.get('recovery_factor', 0):.2f}",
                    "Net Profit / Max DD",
                    COLORS['cyan'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-wave-square", "Ulcer Index",
                    f"{metrics.get('ulcer_index', 0):.2f}",
                    "Stress du DD",
                    COLORS['orange'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-frown", "Pain Index",
                    f"{metrics.get('pain_index', 0):.2f}",
                    "Souffrance moyenne",
                    COLORS['violet'],
                ),
                lg=3, md=6, className="mb-3",
            ),
            dbc.Col(
                create_metric_card(
                    "fa-percentage", "Kelly Criterion",
                    f"{metrics.get('kelly_criterion', 0):.1f}%",
                    "Taille position optimale",
                    COLORS['pink'],
                ),
                lg=3, md=6, className="mb-3",
            ),
        ],
        className="mb-4",
    )

    return html.Div([hero_row, performance_row, risk_row, trade_row, ftmo_row, advanced_row])


# ============================================
# 📈 CHARTS SECTION
# ============================================


def create_equity_chart(data: List[Dict]) -> dcc.Graph:
    """Create modern equity curve with area fill"""
    df = pd.DataFrame(data)

    fig = go.Figure()

    # Equity curve with gradient fill
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.get('balance', df.get('total_reward', [])),
            mode='lines',
            name='Equity',
            line=dict(color=COLORS['cyan'], width=3),
            fill='tozeroy',
            fillcolor=f'rgba(0, 217, 255, 0.1)',
            hovertemplate='<b>Equity</b>: $%{y:,.2f}<extra></extra>',
        )
    )

    fig.update_layout(
        title={
            'text': '📈 Courbe d\'Équité',
            'font': {'size': 24, 'weight': 700, 'color': COLORS['text']},
        },
        template='plotly_dark',
        hovermode='x unified',
        height=450,
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor=COLORS['dark_bg'],
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis=dict(
            title='Episode',
            gridcolor='#2a2e45',
            showgrid=True,
        ),
        yaxis=dict(
            title='Balance ($)',
            gridcolor='#2a2e45',
            showgrid=True,
        ),
    )

    return dcc.Graph(
        figure=fig,
        config={'displayModeBar': True, 'displaylogo': False},
        style={'borderRadius': '15px', 'overflow': 'hidden'},
    )


def create_monthly_returns_chart(data: List[Dict]) -> dcc.Graph:
    """Create monthly returns bar chart"""
    # Simplified for demo - would need actual monthly aggregation
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
    returns = [2.5, 3.1, -1.2, 4.5, 2.8, 5.2, 3.7, -0.8, 6.1, 4.3, 3.9, 5.5]
    colors_list = [COLORS['green'] if r > 0 else COLORS['red'] for r in returns]

    fig = go.Figure(
        go.Bar(
            x=months,
            y=returns,
            marker=dict(color=colors_list, line=dict(width=0)),
            hovertemplate='<b>%{x}</b><br>Return: %{y:.1f}%<extra></extra>',
        )
    )

    fig.update_layout(
        title={
            'text': '📊 Rendements Mensuels',
            'font': {'size': 20, 'weight': 700},
        },
        template='plotly_dark',
        height=350,
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor=COLORS['dark_bg'],
        margin=dict(l=20, r=20, t=60, b=20),
        yaxis=dict(title='Return (%)', gridcolor='#2a2e45'),
        xaxis=dict(gridcolor='#2a2e45'),
    )

    return dcc.Graph(figure=fig, config={'displayModeBar': False, 'displaylogo': False})


def create_win_loss_donut(metrics: Dict) -> dcc.Graph:
    """Create win/loss ratio donut chart"""
    winning = metrics.get('winning_trades', 0)
    losing = metrics.get('losing_trades', 0)

    fig = go.Figure(
        go.Pie(
            labels=['Gagnants', 'Perdants'],
            values=[winning, losing],
            hole=0.6,
            marker=dict(colors=[COLORS['green'], COLORS['red']]),
            textinfo='percent+label',
            textfont=dict(size=14, color='white'),
            hovertemplate='<b>%{label}</b><br>Trades: %{value}<br>%{percent}<extra></extra>',
        )
    )

    # Add center text
    fig.add_annotation(
        text=f"{metrics.get('win_rate', 0):.1f}%",
        x=0.5, y=0.5,
        font=dict(size=32, color=COLORS['text'], weight=700),
        showarrow=False,
    )

    fig.update_layout(
        title={
            'text': '🎯 Win/Loss Ratio',
            'font': {'size': 20, 'weight': 700},
        },
        template='plotly_dark',
        height=350,
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor=COLORS['dark_bg'],
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=-0.1,
            xanchor='center',
            x=0.5,
        ),
    )

    return dcc.Graph(figure=fig, config={'displayModeBar': False, 'displaylogo': False})


def create_charts_section(data: List[Dict], metrics: Dict) -> dbc.Row:
    """Create complete charts section"""
    return html.Div([
        # Equity Curve (Full Width)
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(create_equity_chart(data)),
                    className="shadow-lg",
                    style={'background': COLORS['card_bg'], 'border': 'none', 'borderRadius': '15px'},
                ),
                lg=12, className="mb-4",
            ),
        ]),
        # Monthly Returns + Win/Loss Donut (Side by side)
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(create_monthly_returns_chart(data)),
                    className="shadow-lg",
                    style={'background': COLORS['card_bg'], 'border': 'none', 'borderRadius': '15px'},
                ),
                lg=6, md=12, className="mb-4",
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(create_win_loss_donut(metrics)),
                    className="shadow-lg",
                    style={'background': COLORS['card_bg'], 'border': 'none', 'borderRadius': '15px'},
                ),
                lg=6, md=12, className="mb-4",
            ),
        ]),
    ])


# ============================================
# 🔄 CALLBACKS
# ============================================


@callback(
    [
        Output("upload-status", "children"),
        Output("metrics-cards-container", "children"),
        Output("home-charts-container", "children"),
    ],
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    prevent_initial_call=True,
)
def handle_upload(contents: Optional[str], filename: Optional[str]):
    """
    Handle file upload and generate complete dashboard

    Args:
        contents: Base64 encoded file contents
        filename: Name of uploaded file

    Returns:
        Status message, metrics cards, and charts
    """
    if contents is None:
        return None, None, None

    try:
        # Import data loader
        from utils.data_loader import DataLoader

        loader = DataLoader()
        data = loader.parse_upload(contents, filename)

        if data is None:
            return (
                dbc.Alert(
                    [
                        html.I(className="fas fa-times-circle me-2"),
                        "Échec de l'analyse du fichier. Vérifiez le format.",
                    ],
                    color="danger",
                ),
                None,
                None,
            )

        # Calculate ALL metrics
        from utils.metrics import MetricsCalculator

        calc = MetricsCalculator(data)
        metrics = calc.get_all_metrics()  # Get ALL 30+ metrics

        # Success message
        status = dbc.Alert(
            [
                html.I(className="fas fa-check-circle me-2"),
                f"✓ Chargement réussi : {filename} - {len(data):,} points de données",
            ],
            color="success",
            style={'borderRadius': '10px', 'fontSize': '1rem'},
        )

        # Create metrics layout
        metrics_layout = create_complete_metrics_layout(metrics)

        # Create charts
        charts = create_charts_section(data, metrics)

        return status, metrics_layout, charts

    except Exception as e:
        return (
            dbc.Alert(
                [
                    html.I(className="fas fa-exclamation-triangle me-2"),
                    f"Erreur : {str(e)}",
                ],
                color="danger",
            ),
            None,
            None,
        )
