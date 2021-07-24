
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

sidebar = html.Div(
    [
        html.Img(
            src = "/assets/images/buencafe_icon_1.png",
            className = "sidebarImage"
        ),
        html.Hr(),
        html.H3(
            "Admin", className="adminName"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Boiler", href="/boiler", active="exact"),
                dbc.NavLink("Statistics", href="/statistics", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Settings", href="/settings", active="exact"),
                dbc.NavLink("Add User", href="/new_user", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(
            html.Img(
                src = "/assets/images/mintic_image.png",
                className = "minticImage"
            )
        )
    ],
    className = "sidebar",
)

content = html.Div(id="pageContent", className = "content")


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == '__main__':
    app.run_server(debug=True)