"""
🔀 COMPARISON PAGE - Trading Dashboard Pro
Compare multiple agents/strategies side-by-side
"""

from dash import dcc, html
import dash_bootstrap_components as dbc


def layout():
    """Comparison page layout."""
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                [html.I(className="fas fa-exchange-alt me-3"), "Strategy Comparison"],
                                className="mb-3",
                            ),
                            html.P(
                                "Compare performance across multiple agents and strategies",
                                className="text-muted lead",
                            ),
                        ],
                    ),
                ],
                className="mb-4",
            ),
            # File upload for multiple agents
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(html.H5("Upload Multiple Agents", className="mb-0")),
                                dbc.CardBody(
                                    [
                                        dcc.Upload(
                                            id="upload-comparison",
                                            children=html.Div(
                                                [
                                                    html.I(className="fas fa-folder-open fa-2x mb-2"),
                                                    html.P("Upload multiple ZIP files to compare"),
                                                ],
                                                className="text-center py-3",
                                            ),
                                            style={
                                                "borderWidth": "2px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "10px",
                                            },
                                            multiple=True,
                                        ),
                                    ],
                                ),
                            ],
                            className="shadow-sm mb-3",
                        ),
                    ),
                ],
            ),
            # Comparison results
            html.Div(id="comparison-results"),
        ],
        fluid=True,
    )
