import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div
from app import app

simple_card = dbc.Card(
    [
        dbc.CardImg(src="/../assets/images/Fire.jpg", top=True, style={"border-top-left-radius": "25px", "border-top-right-radius": "25px", "min-height":"20rem", "max-height":"20rem"}),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
            ]
        ),
    ],
    style={"border-radius": "25px", "box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px"},
)

simple_card2 = dbc.Card(
    [
        dbc.CardImg(src="/../assets/images/Cafe_granos.jpg", top=True, style={"border-top-left-radius": "25px", "border-top-right-radius": "25px", "min-height":"20rem", "max-height":"20rem"}),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
            ]
        ),
    ],
    style={"border-radius": "25px", "box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px"},
)

simple_card3 = dbc.Card(
    [
        dbc.CardImg(src="/../assets/images/Pressure.jpg", top=True, style={"border-top-left-radius": "25px", "border-top-right-radius": "25px", "min-height":"20rem", "max-height":"20rem"}),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
            ]
        ),
    ],
    style={"border-radius": "25px", "box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px"},
)


grouped_cards = dbc.Row(
    [
        dbc.Col(simple_card, width=4),
        dbc.Col(simple_card2, width=4),
        dbc.Col(simple_card3, width=4)
    ]
)

layout = [
    html.Div(children = [
        html.Img(
            src = "/assets/images/C1_icon_1.png",
            className = "corr-icon"
        ),
        html.H2(
            "BOILER #6 OPTIMIZATION",
            className = "content-title"
        ),html.Div(grouped_cards, style={'background-color':'transparent',"padding-top":"3rem"}),
        ],
        className = "corr-icon-container"
    ),
]


"""
html.Div(
            children=[html.Div(simple_card, className="card"),
            html.Div(simple_card2, className="card"),
            html.Div(simple_card3, className="card")],
            style={"padding-top": "5em", "background": "green"}
        )"""