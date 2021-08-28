import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app

dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = [

    # html.Div(children = [
    #     html.Img(
    #         src = "/assets/images/C1_icon_1.png",
    #         className = "corr-icon"
    #     ),
    #     html.H2(
    #         "Home",
    #         className = "content-title"
    #     )],
    #     className = "corr-icon-container"
    # ),

    dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "/assets/images/Buencafe_entrada.jpeg",
            "header": "One of the world’s leading premium soluble coffee suppliers",
            #"caption": "One of the world’s leading premium soluble coffee suppliers",
        },
        {
            "key": "2",
            "src": "/assets/images/cafetal.jpeg",
            "header": "Dedicated to providing high-quality coffee, underpinned by an aim to deliver sustainable social impact in the surrounding communities",
        },
        {
            "key": "3",
            "src": "/assets/images/Caldera.jpeg",
            "header": "CHALLENGE: To predict caldera's efficiency",
            #"caption": "With Caption only",
        },
    ],
    controls=False,
    indicators=True,
    
    className="carousel-home",
)
]
