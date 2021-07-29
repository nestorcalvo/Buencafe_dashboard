import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output, ClientsideFunction, State
from app import app

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

layout = [
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
        html.Div([dcc.Graph(id="graph-luis")])
        ],
    className = "corr-icon-container"
    ),

]

@app.callback(
    Output('graph-luis','figure'),
    Input('url','pathname')
)
def plot_fig1(pathname):
    df_luis = px.data.stocks()
    fig_luis = px.line(df_luis, x='date', y="GOOG",
                labels={
                    "date": "Date",
                    "GOOG": "Steam Generation (Ton/day)",
                },
                title="Steam Generation")
    fig_luis.update_layout(transition_duration=500)
    return fig_luis
