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
                                        html.H5("Average Speed"),
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
                                        html.H5("Average Power"),
                                        html.H5("Small Box 2"),
                                        html.H5("Small Box 2"),
                                        html.H5("Small Box 2"),
                                        html.H5("Small Box 2"),
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
                                        html.H5("Average HR."),
                                        html.H5("Small Box 3"),
                                        html.H5("Small Box 3"),
                                        html.H5("Small Box 3"),
                                        html.H5("Small Box 3"),
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
                                        html.H5("Controls"),
                                        controls["year_dropdown"],
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
                                        html.H5("Controls"),
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
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
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


"""
ALTERNATIV 1:
def get_bike_stats_layout():
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
                                        html.H5("Small Box 1"),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H5("Small Box 2"),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H5("Small Box 3"),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H5("Small Box 4"),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=3,
                    ),
                ],
                className="sport-type-stats-card",
            ),
            dbc.Row(
                [
                    # Large box spanning 2 rows and 3 columns
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Div(
                                    children=[
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                        html.H5("Large box spanning"),
                                    ],
                                    className="text-center",
                                )
                            ),
                            color="light",
                        ),
                        width=9,
                        style={"grid-row": "span 2"},  # Span across 2 rows
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            html.Div(
                                                children=[
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
                                                    html.H5("Small Box 6"),
                                                ],
                                                className="text-center",
                                            )
                                        ),
                                        color="light",
                                    ),
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
"""
