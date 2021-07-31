import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import date
from dash.dependencies import Input, Output, ClientsideFunction, State
from app import app

layout= [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "Water Analitycs",
            className = "content-title"
        ),
        html.P(
            "Select date range that you want to see:"
        )
        ,
        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=date(2018, 2, 6),
            max_date_allowed=date(2019, 6, 30),
            initial_visible_month=date(2018, 2, 6),
            end_date=date(2019, 6, 30),
            clearable=True,
            month_format="MMMM, YYYY",
            number_of_months_shown=3
        ),
        html.Div(id='output-container-date-picker-range',
            className="month-container")
        ,
        dcc.Graph(id="graph-luis")
        ],
    className = "corr-icon-container"
    ),

]

@app.callback(
    Output('graph-luis','figure'),
    [Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')]
)

def update_figure(start_date, end_date) :
    df = px.data.stocks()
    df.index = df["date"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = df.loc[start_date: end_date]["date"],
        y = df.loc[start_date: end_date]["GOOG"],
        mode = "lines",
        name = "Steam"
    ))
    fig.update_layout(title = 'Steam Generation',
                    xaxis_title='Date',
                    yaxis_title='Steam (Ton/day)',
                    transition_duration=500)
    return fig