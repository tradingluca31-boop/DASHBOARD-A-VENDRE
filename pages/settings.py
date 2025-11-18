"""
⚙️ SETTINGS PAGE - Trading Dashboard Pro
User preferences and configuration
"""

from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


def layout():
    """Settings page layout."""
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                [html.I(className="fas fa-cog me-3"), "Settings"],
                                className="mb-3",
                            ),
                            html.P(
                                "Customize your dashboard experience",
                                className="text-muted lead",
                            ),
                        ],
                    ),
                ],
                className="mb-4",
            ),
            # Settings sections
            dbc.Row(
                [
                    dbc.Col(
                        [
                            # Display settings
                            dbc.Card(
                                [
                                    dbc.CardHeader(html.H5("Display Preferences", className="mb-0")),
                                    dbc.CardBody(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            dbc.Label("Theme"),
                                                            dbc.Select(
                                                                id="theme-select",
                                                                options=[
                                                                    {"label": "Dark (Default)", "value": "dark"},
                                                                    {"label": "Light", "value": "light"},
                                                                ],
                                                                value="dark",
                                                            ),
                                                        ],
                                                        md=6,
                                                    ),
                                                    dbc.Col(
                                                        [
                                                            dbc.Label("Auto-Refresh"),
                                                            dbc.Select(
                                                                id="refresh-select",
                                                                options=[
                                                                    {"label": "Disabled", "value": "0"},
                                                                    {"label": "30 seconds", "value": "30"},
                                                                    {"label": "60 seconds", "value": "60"},
                                                                    {"label": "5 minutes", "value": "300"},
                                                                ],
                                                                value="0",
                                                            ),
                                                        ],
                                                        md=6,
                                                    ),
                                                ],
                                                className="mb-3",
                                            ),
                                            dbc.Checklist(
                                                id="display-options",
                                                options=[
                                                    {"label": "Show grid lines", "value": "grid"},
                                                    {"label": "Enable tooltips", "value": "tooltips"},
                                                    {"label": "Compact view", "value": "compact"},
                                                ],
                                                value=["grid", "tooltips"],
                                                switch=True,
                                            ),
                                        ],
                                    ),
                                ],
                                className="shadow-sm mb-3",
                            ),
                            # Export settings
                            dbc.Card(
                                [
                                    dbc.CardHeader(html.H5("Export Options", className="mb-0")),
                                    dbc.CardBody(
                                        [
                                            dbc.Label("Default Format"),
                                            dbc.RadioItems(
                                                id="export-format",
                                                options=[
                                                    {"label": "PDF Report", "value": "pdf"},
                                                    {"label": "Excel (.xlsx)", "value": "xlsx"},
                                                    {"label": "CSV", "value": "csv"},
                                                    {"label": "JSON", "value": "json"},
                                                ],
                                                value="pdf",
                                            ),
                                            html.Hr(),
                                            dbc.Button(
                                                [html.I(className="fas fa-download me-2"), "Export Current Data"],
                                                id="export-button",
                                                color="primary",
                                                className="w-100",
                                            ),
                                        ],
                                    ),
                                ],
                                className="shadow-sm mb-3",
                            ),
                            # License info (for selling)
                            dbc.Card(
                                [
                                    dbc.CardHeader(html.H5("License Information", className="mb-0")),
                                    dbc.CardBody(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col([dbc.Label("Status:"), html.P("Active", className="text-success fw-bold")]),
                                                    dbc.Col([dbc.Label("Expires:"), html.P("2025-12-31")]),
                                                ],
                                            ),
                                            html.Hr(),
                                            dbc.Button(
                                                [html.I(className="fas fa-key me-2"), "Manage License"],
                                                color="secondary",
                                                outline=True,
                                                className="w-100",
                                            ),
                                        ],
                                    ),
                                ],
                                className="shadow-sm",
                            ),
                        ],
                        lg=8,
                        className="mx-auto",
                    ),
                ],
            ),
        ],
        fluid=True,
    )
