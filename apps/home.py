import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
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
            "src": "/assets/images/Overview.png",
            "header": "With header ",
            "caption": "and caption",
        },
        {
            "key": "2",
            "src": "/assets/images/Cofficiency.png",
            "header": "With header only",
            "caption": "",
        },
        {
            "key": "3",
            "src": "https://www.colorpsychology.org/es/wp-content/uploads/2019/07/azul-color.png",
            "header": "",
            "caption": "With Caption only",
        },
    ],
    controls=True,
    indicators=True,
    className="carousel-home",
)
]