
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div(children = [

    html.H1(children = 'Basic app')
]
)

if __name__ == '__main__':
    app.run_server(debug=True)