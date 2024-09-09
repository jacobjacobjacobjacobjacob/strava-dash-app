# dashapp/components/navbar.py
from dash import dcc, html
import dash_bootstrap_components as dbc


from dashapp.components.ids import REFRESH_DATA_BUTTON

navbar = dbc.NavbarSimple(
    children=[
        dbc.Container(
            [
                dbc.NavbarBrand("STRAVA DASHBOARD", href="/"),
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dcc.Link("OVERVIEW", href="/", className="nav-link")
                        ),
                        dbc.NavItem(
                            dcc.Link(
                                "LAST ACTIVITY",
                                href="/last_activity",
                                className="nav-link",
                            )
                        ),
                        dbc.NavItem(
                            dcc.Link(
                                "GOALS",
                                href="/goals",
                                className="nav-link",
                            )
                        ),
                        dbc.NavItem(
                            dcc.Link(
                                "COMPARE",
                                href="/compare",
                                className="nav-link",
                            )
                        ),
                        dbc.NavItem(
                            dbc.DropdownMenu(
                                label="STATS",
                                nav=True,
                                in_navbar=True,
                                children=[
                                    dbc.DropdownMenuItem(
                                        dcc.Link(
                                            "Bike",
                                            href="/stats/bike",
                                            className="dropdown-item",
                                        )
                                    ),
                                    dbc.DropdownMenuItem(
                                        dcc.Link(
                                            "Run",
                                            href="/stats/run",
                                            className="dropdown-item",
                                        )
                                    ),
                                    dbc.DropdownMenuItem(
                                        dcc.Link(
                                            "Health",
                                            href="/stats/health",
                                            className="dropdown-item",
                                        )
                                    ),
                                ],
                            )
                        ),
                        dbc.NavItem(
                            dcc.Link("DATA", href="/data", className="nav-link")
                        ),
                    ],
                    className="d-flex justify-content-center",
                ),
                dbc.Button(
                    html.I(className="fa-solid fa-arrows-rotate"),
                    outline=False,
                    color="light",
                    size="sm",
                    className="me-1",
                    id=REFRESH_DATA_BUTTON,
                ),
                html.Div(id="alert-div"),
            ],
            className="d-flex justify-content-between align-items-center",
        ),
    ],
    brand="",
    brand_href="#",
    color="primary",
    dark=True,
    className="navbar-custom",
)
