"""
🏠 HOME PAGE - Trading Dashboard Pro
Main overview page with key metrics and quick insights
"""

from typing import Optional, List, Dict
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

# ============================================
# 📐 PAGE LAYOUT
# ============================================


def layout():
    """
    Home page layout with:
    - File upload section
    - Key metrics cards
    - Equity curve chart
    - Recent performance summary
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
                                    "Dashboard Overview",
                                ],
                                className="mb-3",
                            ),
                            html.P(
                                "Upload your trading data and monitor performance in real-time",
                                className="text-muted lead",
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
                                            "Upload Trading Data",
                                        ],
                                        className="mb-0",
                                    ),
                                ),
                                dbc.CardBody(
                                    [
                                        dcc.Upload(
                                            id="upload-data",
                                            children=html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-cloud-upload-alt fa-3x mb-3 text-primary"
                                                    ),
                                                    html.H5("Drag & Drop or Click to Upload"),
                                                    html.P(
                                                        "Supports: ZIP, JSON, CSV files",
                                                        className="text-muted small mb-0",
                                                    ),
                                                ],
                                                className="text-center py-4",
                                            ),
                                            style={
                                                "borderWidth": "2px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "10px",
                                                "borderColor": "#555",
                                                "background": "#1a1a1a",
                                            },
                                            multiple=False,
                                        ),
                                        html.Div(id="upload-status", className="mt-3"),
                                    ],
                                ),
                            ],
                            className="shadow-sm mb-4",
                        ),
                        lg=8,
                        className="mx-auto",
                    ),
                ],
            ),
            # Metrics Cards Row
            html.Div(id="metrics-cards-container"),
            # Charts Section
            html.Div(id="home-charts-container"),
        ],
        fluid=True,
    )


# ============================================
# 📊 METRICS CARDS COMPONENT
# ============================================


def create_metrics_cards(data: Dict) -> dbc.Row:
    """
    Create metric cards from data.

    Args:
        data: Dictionary with metrics

    Returns:
        Bootstrap row with metric cards
    """
    metrics = [
        {
            "icon": "fa-dollar-sign",
            "label": "Equity",
            "value": f"${data.get('equity', 0):,.2f}",
            "delta": f"+{data.get('roi', 0):.2f}%",
            "color": "success" if data.get("roi", 0) > 0 else "danger",
        },
        {
            "icon": "fa-chart-line",
            "label": "Total Return",
            "value": f"{data.get('roi', 0):.2f}%",
            "delta": f"${data.get('total_pnl', 0):,.2f}",
            "color": "success" if data.get("roi", 0) > 0 else "danger",
        },
        {
            "icon": "fa-percentage",
            "label": "Win Rate",
            "value": f"{data.get('win_rate', 0):.1f}%",
            "delta": f"{data.get('total_trades', 0)} trades",
            "color": "info",
        },
        {
            "icon": "fa-balance-scale",
            "label": "Profit Factor",
            "value": f"{data.get('profit_factor', 0):.2f}",
            "delta": "Target: > 1.5",
            "color": "success" if data.get("profit_factor", 0) > 1.5 else "warning",
        },
        {
            "icon": "fa-chart-area",
            "label": "Sharpe Ratio",
            "value": f"{data.get('sharpe_ratio', 0):.2f}",
            "delta": "Target: > 1.0",
            "color": "success" if data.get("sharpe_ratio", 0) > 1.0 else "warning",
        },
        {
            "icon": "fa-arrow-down",
            "label": "Max Drawdown",
            "value": f"{data.get('max_drawdown_pct', 0):.2f}%",
            "delta": "FTMO: < 10%",
            "color": "success" if data.get("max_drawdown_pct", 0) < 10 else "danger",
        },
    ]

    cards = []
    for metric in metrics:
        card = dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    html.I(className=f"fas {metric['icon']} fa-2x text-{metric['color']}"),
                                ],
                                className="mb-3",
                            ),
                            html.H6(metric["label"], className="text-muted mb-2"),
                            html.H3(metric["value"], className="mb-2"),
                            html.P(
                                metric["delta"],
                                className=f"small mb-0 text-{metric['color']}",
                            ),
                        ],
                    ),
                ],
                className="shadow-sm h-100 border-start border-5 border-" + metric["color"],
            ),
            lg=2,
            md=4,
            sm=6,
            className="mb-3",
        )
        cards.append(card)

    return dbc.Row(cards, className="mb-4")


# ============================================
# 📈 EQUITY CURVE CHART
# ============================================


def create_equity_chart(data: List[Dict]) -> dcc.Graph:
    """
    Create interactive equity curve chart.

    Args:
        data: List of checkpoint data

    Returns:
        Plotly graph component
    """
    df = pd.DataFrame(data)

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.7, 0.3],
        subplot_titles=("Equity Curve", "Drawdown %"),
    )

    # Equity curve
    fig.add_trace(
        go.Scatter(
            x=df["timestep"],
            y=df["balance"],
            mode="lines",
            name="Equity",
            line=dict(color="#00d4ff", width=2),
            fill="tozeroy",
            fillcolor="rgba(0, 212, 255, 0.1)",
        ),
        row=1,
        col=1,
    )

    # Drawdown
    fig.add_trace(
        go.Scatter(
            x=df["timestep"],
            y=df["drawdown_pct"],
            mode="lines",
            name="Drawdown %",
            line=dict(color="#ff4444", width=2),
            fill="tozeroy",
            fillcolor="rgba(255, 68, 68, 0.1)",
        ),
        row=2,
        col=1,
    )

    # FTMO line at -10%
    fig.add_hline(
        y=-10,
        line_dash="dash",
        line_color="red",
        annotation_text="FTMO Limit",
        row=2,
        col=1,
    )

    # Layout
    fig.update_layout(
        height=600,
        template="plotly_dark",
        hovermode="x unified",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=60, b=20),
    )

    fig.update_xaxes(title_text="Timesteps", row=2, col=1)
    fig.update_yaxes(title_text="Balance ($)", row=1, col=1)
    fig.update_yaxes(title_text="Drawdown (%)", row=2, col=1)

    return dcc.Graph(figure=fig, config={"displayModeBar": True, "displaylogo": False})


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
    Handle file upload and process data.

    Args:
        contents: Base64 encoded file contents
        filename: Name of uploaded file

    Returns:
        Upload status, metrics cards, and charts
    """
    if contents is None:
        return None, None, None

    try:
        # Import here to avoid circular dependency
        from utils.data_loader import DataLoader

        loader = DataLoader()
        data = loader.parse_upload(contents, filename)

        if data is None:
            return (
                dbc.Alert("Failed to parse file. Please check format.", color="danger"),
                None,
                None,
            )

        # Calculate metrics
        from utils.metrics import MetricsCalculator

        calc = MetricsCalculator(data)
        metrics = calc.get_summary_metrics()

        # Create components
        status = dbc.Alert(
            [
                html.I(className="fas fa-check-circle me-2"),
                f"Successfully loaded {filename} - {len(data):,} checkpoints",
            ],
            color="success",
        )

        cards = create_metrics_cards(metrics)
        chart = dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                html.H5(
                                    [html.I(className="fas fa-chart-line me-2"), "Performance"],
                                    className="mb-0",
                                ),
                            ),
                            dbc.CardBody(create_equity_chart(data)),
                        ],
                        className="shadow-sm",
                    ),
                ),
            ],
            className="mb-4",
        )

        return status, cards, chart

    except Exception as e:
        return (
            dbc.Alert(f"Error: {str(e)}", color="danger"),
            None,
            None,
        )
