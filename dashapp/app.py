# dashapp/app.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

from main import main
from assets.config import STRAVA_DATA_PATH
from api.update_data import fetch_strava_data

from dashapp.components.controls import *

from dashapp.layouts.overview import get_overview_layout
from dashapp.layouts.goals import get_goals_layout
from dashapp.layouts.bike_stats import get_bike_stats_layout

from dashapp.callbacks.overview_callbacks import register_overview_callbacks
from dashapp.callbacks.bike_stats_callbacks import register_bike_stats_callbacks


"""
DASHBOARD
"""

# Load Strava Data
#fetch_strava_data()
#df = main()
df = pd.read_csv(STRAVA_DATA_PATH)


# Create the Dash app
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        #dbc.themes.COSMO,
        #dbc.themes.YETI,
        dbc.themes.MINTY,
        dbc.icons.FONT_AWESOME,
    ],
)

server = app.server

# Set up the layout with a placeholder for dynamic content
app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Store(id="pathname-store"),
        html.Div(id="page-content"),
    ]
)


# Button to update Strava data
@app.callback(
    Output("alert-div", "children"),
    Input(REFRESH_DATA_BUTTON, "n_clicks"),
    prevent_initial_call=True,
)
def update_data(n_clicks):
    if n_clicks:
        fetch_strava_data()
        main()
        df = pd.read_csv(STRAVA_DATA_PATH)
        return dbc.Alert(
            "Data updated.",
            color="success",
            dismissable=True,
            duration=1000,
        )
    return ""


# Layout Specific Callbacks
register_overview_callbacks(app, df)
register_bike_stats_callbacks(app, df)


# Callback to dynamically change page content based on URL pathname
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname: str):
    if pathname == "/":
        return get_overview_layout(
            month_checklist=get_month_checklist(df),
            year_checklist=get_year_checklist(df),
            sport_type_checklist=get_sport_type_checklist(df),
            month_filtering_button_group=get_month_filtering_button_group(),
        )
    elif pathname == "/last_activity":
        pass
    elif pathname == "/goals":
        return get_goals_layout(df)

    elif pathname == "/stats/bike":
        return get_bike_stats_layout(
            year_dropdown=get_year_dropdown(df),
            bike_metrics_checklist=get_bike_metrics_checklist(df),
            environment_checklist=get_environment_checklist(df),
        )
    elif pathname == "/stats/run":
        pass
    elif pathname == "/data":
        pass
    else:
        return html.H1("PAGE NOT FOUND")
