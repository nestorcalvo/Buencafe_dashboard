import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
from app import app


graph_1 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)

graph_2 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)

graph_3 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)

graph_4 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)

graph_5 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)

graph_6 =  dbc.Card(children=[
        dbc.CardHeader(children=["Card Header"]),
        dbc.CardBody([html.H5("Card title", className="card-title"),
            html.P("This is some card content that we'll reuse",
                className="card-text")
                ]
                )
    ],
    style={"min-height":"20rem","max-height":"20rem"}
)


grouped_cards = html.Div(children=[
        dbc.Row([dbc.Col(graph_2, style={'padding-top':'2rem'}),
                dbc.Col(graph_3, style={'padding-top':'2rem'})]),
        dbc.Row([dbc.Col(graph_2, style={'padding-top':'2rem'}),
                dbc.Col(graph_3, style={'padding-top':'2rem'})]),
        dbc.Row([dbc.Col(graph_2, style={'padding-top':'2rem'}),
                dbc.Col(graph_3, style={'padding-top':'2rem'})])
        ])
        
layout = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "About Us",
            className = "content-title"
        ),
        grouped_cards],
        className = "corr-icon-container"
    ),
]