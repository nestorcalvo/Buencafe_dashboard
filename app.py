
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from flask import Flask

from dash.dependencies import Input, Output,ClientsideFunction, State
external_scripts =[
    {
        # Icons libraries
        'src': 'https://kit.fontawesome.com/b359ae410d.js',
        'crossorigin': 'anonymous'
    }
]
server = Flask(__name__)
app = dash.Dash(__name__,server = server,external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=external_scripts)
server = app.server
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True

app.title = "Buencafé Dashboard"
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"]
#menus desplegables de manera vertical
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

#Dataframe y grafica
df_luis = px.data.stocks()
fig_luis = px.line(df_luis, x='date', y="GOOG",
                labels={
                     "date": "Date",
                     "GOOG": "Steam Generation (Ton/day)",
                 },
                title="Steam Generation")


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

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id='page-content', className = 'content')
])


layout_boiler = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "OPTIMIZATION OF THE STEAM BOILER OPERATION FOR BUENCAFE LIOFILIZADO DE COLOMBIA",
            className = "content-title"
        ),
        dbc.Container([
            dbc.Row([
                dbc.Col(control_1, md=2),
                dbc.Col(control_2, md=2)],
            align="left")],
            fluid=True,
            className = "month-container"
        ),
        html.Div([dcc.Graph(figure=fig_luis)])
        ],
    className = "corr-icon-container"
    ),

]

layout_statistics = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "BOILER #6 OPTIMIZATION",
            className = "content-title"
        )],
        className = "corr-icon-container"
    ),
]

@app.callback(     
    Output('page-content','children'),
    Input('url','pathname')
)
def layout_selectio(pathname):
    if pathname == '/boiler':
        return layout_boiler
    elif pathname == '/statistics':
        return layout_statistics
    else:
        return html.Div()

app.layout = url_bar_and_content_div

app.validation_layout = html.Div([
    url_bar_and_content_div,
    sidebar,
    layout_boiler,
    layout_statistics,
])

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)
#    app.run_server(debug=True, host ='0.0.0.0', port = 8050, dev_tools_hot_reload=False)



