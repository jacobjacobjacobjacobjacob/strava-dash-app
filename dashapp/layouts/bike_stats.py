# dashapp/layouts/overview.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from dashapp.components.navbar import navbar
from dashapp.components.ids import *

""" 
BIKE STATS
"""


def get_bike_stats_layout(**controls):
    return dbc.Container(
        [
            # Navbar
            navbar,
            dbc.Row(
                [
                    # Top row with 4 small boxes
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H4("Speed (kph)"),
                                        dcc.Graph(
                                            id=BIKE_STATS_AVERAGE_SPEED_LINE_CHART,
                                            style={
                                                "width": "450px",
                                            },
                                        ),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H4("Power (w)"),
                                        dcc.Graph(
                                            id=BIKE_STATS_AVERAGE_POWER_LINE_CHART,
                                            style={
                                                "width": "450px",
                                            },
                                        ),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H4("Heartrate (bpm)"),
                                        dcc.Graph(
                                            id=BIKE_STATS_AVERAGE_HR_LINE_CHART,
                                            style={
                                                "width": "450px",
                                            },
                                        ),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=4,
                    ),
                ],
                className="sport-type-stats-card",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H4("Controls"),
                                        html.H5("Year"),
                                        controls["year_dropdown"],
                                        html.Br(),
                                        html.H5("Metrics"),
                                        controls["bike_metrics_checklist"],
                                        html.Br(),
                                        html.H5("Environment"),
                                        controls["environment_checklist"],
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=2,
                        className="sport-type-stats-card",
                    ),
                    # Large box spanning 2 rows and 3 columns
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H4("Comparison"),
                                        dcc.Graph(
                                            id=BIKE_STATS_COMPARISON_CHART,
                                            style={
                                                "width": "700px",
                                            },
                                        ),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=7,
                        style={"grid-row": "span 2"},
                        className="sport-type-stats-card",
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            html.Div(
                                                children=[
                                                    html.H5("Suffer Score"),
                                                    html.H5("Radar"),
                                                    html.H5("Polar"),
                                                    html.H5("Buckets"),
                                                    html.H5("Small Box 5"),
                                                    html.H5("Small Box 5"),
                                                ],
                                                className="text-center",
                                            )
                                        ),
                                        color="light",
                                    ),
                                    className="sport-type-stats-card",
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            html.Div(
                                                children=[
                                                    html.H5("Activities"),
                                                    html.H5("Indoor"),
                                                    html.H5("vs"),
                                                    html.H5("Outdoor"),
                                                    html.H5("Small Box 6"),
                                                ],
                                                className="text-center",
                                            )
                                        ),
                                        color="light",
                                    ),
                                    className="sport-type-stats-card",
                                ),
                            ),
                        ],
                        width=3,
                    ),
                ],
            ),
        ],
        fluid=True,
    )
