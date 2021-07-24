
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_scripts =[
    {
        # Icons libraries
        'src': 'https://kit.fontawesome.com/b359ae410d.js',
        'crossorigin': 'anonymous'
    }
]
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"]

control_1 = dbc.Card(
    [
        dbc.FormGroup([
            dbc.Label("Begining Month"),
            dcc.Dropdown(
                id = "begining-month",
                options = [{
                    "label": col,
                    "value": col
                } for col in months],
                value="January"
            )
        ])
    ]
)
control_2 = dbc.Card(
    [
        dbc.FormGroup([
            dbc.Label("Ending Month"),
            dcc.Dropdown(
                id = "ending-month",
                options = [{
                    "label": col,
                    "value": col
                } for col in months],
                value="February"
            )
        ])
    ]
)

sidebar = html.Div(
    [
        html.Img(
            src = "/assets/images/buencafe_icon_1.png",
            className = "sidebar-image"
        ),
        html.I(
            className = "fas fa-user-tie"
        ),
        html.H3(
            "Admin", className="admin-name"
        ),
        html.Hr(),
        dbc.Nav(
            [
                html.Div(
                    children = [
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-industry"), "Boiler"
                            ], 
                            href="/boiler", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                ),

                html.Div(
                    children=[
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-chart-bar"),"Statistics"
                            ], 
                            href="/statistics", active="exact"
                        ),
                    ],
                    className = "nav-icon-link"
                ),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        dbc.Nav(
            [
                html.Div(
                    children = [
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-cogs"), "Settings"
                            ], 
                            href="/settings", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                ),

                html.Div(
                    children=[
                        dbc.NavLink(
                            [
                                html.I(className = "far fa-plus-square"),"Add User"
                            ], 
                            href="/new_user", active="exact"
                        ),
                    ],
                    className = "nav-icon-link"
                ),
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(
            html.Img(
                src = "/assets/images/mintic_image.png",
                className = "mintic-image"
            )
        )
    ],
    className = "sidebar",
)

content = html.Div(
    [
        html.Div(
            html.Img(
                src = "/assets/images/C1_icon_1.png",
                className = "corr-icon"
            ),
            className = "corr-icon-container"
        ),
        html.H1(
            "OPTIMIZATION OF THE STEAM BOILER OPERATION FOR BUENCAFE LIOFILIZADO DE COLOMBIA",
            className = "content-title"
        ),
        dbc.Container([
            dbc.Row([
                dbc.Col(control_1, md=3),
                dbc.Col(control_2, md=3)
                ],
                align="left"
                )
                ],
            fluid=True)
    ],
    id="page-content", 
    className = "content")


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == '__main__':
    app.run_server(debug=True)