"""
📊 ANALYTICS PAGE - Trading Dashboard Pro
Advanced analytics with detailed metrics breakdown
"""

from dash import dcc, html
import dash_bootstrap_components as dbc


def layout():
    """Analytics page layout."""
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                [html.I(className="fas fa-chart-bar me-3"), "Advanced Analytics"],
                                className="mb-3",
                            ),
                            html.P(
                                "Deep dive into performance metrics and statistical analysis",
                                className="text-muted lead",
                            ),
                        ],
                    ),
                ],
                className="mb-4",
            ),
            # Metrics breakdown section
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(html.H5("Risk Metrics", className="mb-0")),
                                dbc.CardBody(
                                    [
                                        html.P("Sharpe Ratio, Sortino, Calmar, VaR analysis"),
                                        html.Div(id="risk-metrics-content"),
                                    ],
                                ),
                            ],
                            className="shadow-sm mb-3",
                        ),
                        lg=6,
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(html.H5("Trade Statistics", className="mb-0")),
                                dbc.CardBody(
                                    [
                                        html.P("Win rate, profit factor, expectancy"),
                                        html.Div(id="trade-stats-content"),
                                    ],
                                ),
                            ],
                            className="shadow-sm mb-3",
                        ),
                        lg=6,
                    ),
                ],
            ),
            # Charts section
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(html.H5("Returns Distribution", className="mb-0")),
                                dbc.CardBody(html.Div(id="returns-distribution-chart")),
                            ],
                            className="shadow-sm",
                        ),
                        lg=12,
                        className="mb-3",
                    ),
                ],
            ),
        ],
        fluid=True,
    )
