
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}


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
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Boiler", href="/boiler", active="exact"),
                dbc.NavLink("Statistics", href="/statistics", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className = "sidebar",
)

content = html.Div(id="pageContent", style=CONTENT_STYLE)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == '__main__':
    app.run_server(debug=True)