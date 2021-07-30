import dash
import dash_html_components as html
from app import app

layout = [
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