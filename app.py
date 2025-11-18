"""
🏛️ TRADING DASHBOARD PRO - Main Application
Professional-grade trading analytics dashboard built with Plotly Dash

Author: Your Company Name
License: Commercial (requires activation)
Version: 1.0.0
"""

import os
from pathlib import Path
from typing import Optional

import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import custom components
from utils.auth import AuthManager
from utils.data_loader import DataLoader
from utils.metrics import MetricsCalculator
from pages import home, analytics, comparison, settings

# ============================================
# 🎨 APP CONFIGURATION
# ============================================

# Dash Bootstrap theme - Professional dark theme
external_stylesheets = [
    dbc.themes.CYBORG,  # Dark professional theme
    dbc.icons.FONT_AWESOME,  # Icons
]

# Initialize Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    title="Trading Dashboard Pro",
    update_title="Updating...",
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

# For deployment
server = app.server

# ============================================
# 🔐 AUTHENTICATION SETUP (Optional)
# ============================================

ENABLE_AUTH = os.getenv("ENABLE_AUTH", "False") == "True"

if ENABLE_AUTH:
    auth_manager = AuthManager()
    # Will be implemented in utils/auth.py

# ============================================
# 📐 LAYOUT - Main Structure
# ============================================

# Navigation Bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.I(className="fas fa-chart-line me-2"),
                                html.Span("Trading Dashboard Pro", className="navbar-brand"),
                            ],
                            className="d-flex align-items-center",
                        ),
                        width="auto",
                    ),
                ],
                align="center",
                className="g-0 w-100",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Home", href="/", id="nav-home")),
                                dbc.NavItem(dbc.NavLink("Analytics", href="/analytics", id="nav-analytics")),
                                dbc.NavItem(dbc.NavLink("Comparison", href="/comparison", id="nav-comparison")),
                                dbc.NavItem(dbc.NavLink("Settings", href="/settings", id="nav-settings")),
                            ],
                            navbar=True,
                            className="ms-auto",
                        ),
                        width="auto",
                    ),
                ],
                align="center",
                className="g-0 w-100",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.I(className="fas fa-circle text-success me-2", id="status-indicator"),
                                html.Span("Connected", id="status-text", className="small"),
                            ],
                            className="d-flex align-items-center",
                        ),
                        width="auto",
                    ),
                ],
                align="center",
                className="g-0",
            ),
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
    sticky="top",
    className="mb-4 shadow",
)

# Footer
footer = dbc.Container(
    [
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.P(
                        [
                            "© 2025 Trading Dashboard Pro | ",
                            html.A("Documentation", href="/docs", className="text-decoration-none"),
                            " | ",
                            html.A("Support", href="/support", className="text-decoration-none"),
                        ],
                        className="text-muted small text-center mb-0",
                    ),
                ),
            ],
        ),
    ],
    fluid=True,
    className="mt-5 py-3",
)

# Main Layout
app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        dbc.Container(id="page-content", fluid=True),
        footer,
        # Store components for data persistence
        dcc.Store(id="session-data", storage_type="session"),
        dcc.Store(id="user-preferences", storage_type="local"),
        # Interval for auto-refresh
        dcc.Interval(
            id="interval-component",
            interval=30 * 1000,  # 30 seconds
            n_intervals=0,
            disabled=True,  # Disabled by default
        ),
    ],
    fluid=True,
    className="px-0",
)

# ============================================
# 📍 ROUTING CALLBACKS
# ============================================


@callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname: Optional[str]):
    """
    Route to different pages based on URL pathname.

    Args:
        pathname: Current URL path

    Returns:
        Page layout component
    """
    if pathname == "/" or pathname is None:
        return home.layout()
    elif pathname == "/analytics":
        return analytics.layout()
    elif pathname == "/comparison":
        return comparison.layout()
    elif pathname == "/settings":
        return settings.layout()
    else:
        # 404 page
        return dbc.Container(
            [
                dbc.Row(
                    dbc.Col(
                        [
                            html.H1("404", className="display-1 text-danger"),
                            html.H3("Page Not Found"),
                            html.P("The page you're looking for doesn't exist."),
                            dbc.Button("Go Home", href="/", color="primary", size="lg"),
                        ],
                        className="text-center my-5",
                    ),
                ),
            ],
        )


@callback(
    [
        Output("nav-home", "active"),
        Output("nav-analytics", "active"),
        Output("nav-comparison", "active"),
        Output("nav-settings", "active"),
    ],
    Input("url", "pathname"),
)
def update_nav_active(pathname: Optional[str]):
    """Update active state of navigation links."""
    if pathname == "/" or pathname is None:
        return True, False, False, False
    elif pathname == "/analytics":
        return False, True, False, False
    elif pathname == "/comparison":
        return False, False, True, False
    elif pathname == "/settings":
        return False, False, False, True
    return False, False, False, False


# ============================================
# 🚀 RUN SERVER
# ============================================

if __name__ == "__main__":
    # Get configuration from environment
    debug_mode = os.getenv("DEBUG_MODE", "True") == "True"
    port = int(os.getenv("PORT", "8050"))

    print("=" * 60)
    print("🏛️  TRADING DASHBOARD PRO - Starting...")
    print("=" * 60)
    print(f"📍 URL: http://localhost:{port}")
    print(f"🔧 Debug Mode: {debug_mode}")
    print(f"🔐 Authentication: {'Enabled' if ENABLE_AUTH else 'Disabled'}")
    print("=" * 60)

    app.run_server(
        debug=debug_mode,
        host="0.0.0.0",  # Allow external connections
        port=port,
    )
