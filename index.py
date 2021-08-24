import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_loading_spinners as dls
from app import app
from app import server
import functools
from apps import water, settings, fuel, efficiency, home, about


app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "Buencafé Dashboard"

sidebar = html.Div(
    [
        html.Img(
            src = "/assets/images/buencafe_icon_1.png",
            className = "sidebar-image"
        ),
        dbc.Nav(
            [
                html.Div(
                    children = [
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-house-user"), "Home"
                            ], 
                            href="/apps/home", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                )
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        
        html.Div([
            html.H4("Analytics")
        ]),
        dbc.Nav(
            [
                html.Div(
                    children = [
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-faucet"), "Water"
                            ], 
                            href="/apps/water", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                ),

                html.Div(
                    children=[
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-gas-pump"),"Fuel"
                            ], 
                            href="/apps/fuel", active="exact"
                        ),
                    ],
                    className = "nav-icon-link"
                ),

                html.Div(
                    children = [
                        dbc.NavLink(
                            [
                                html.I(className = "fas fa-percentage"), "Efficiency"
                            ], 
                            href="/apps/efficiency", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                )
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
                            href="/apps/settings", active="exact"
                        )
                    ],
                    className = "nav-icon-link"
                ),

                html.Div(
                    children=[
                        dbc.NavLink(
                            [
                                html.I(className = "far fa-address-card"),"About us"
                            ], 
                            href="/apps/aboutus", active="exact"
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
        ),
        
    ],
    className = "sidebar",
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    #html.Div(id='background-content', className = 'background-content', children = []),
    html.Div(id='page-content', className = 'content', children = []),
    # dls.Hash(
    #     html.Div(id='page-content', className = 'content', children = []),
    #     size = 160,
    #     speed_multiplier = 0.8,
    #     debounce = 1000
    # )
], className = "top-layout")

@app.callback(     
    Output('page-content','children'),
    Input('url','pathname')
)
@functools.lru_cache(maxsize=32)
def layout_selection(pathname):
    # for value in range(0,20000):
    #     print(value)
    #print(dash.callback_context.triggered)
    if pathname == '/apps/water':
        return water.layout
    elif pathname == '/apps/home':
        return home.layout
    elif pathname == '/apps/fuel':
        return fuel.layout
    elif pathname == '/apps/efficiency':
        return efficiency.layout
    elif pathname == '/apps/aboutus':
        return about.layout
    else:
        return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)
    #app.run_server(debug=True, host ='0.0.0.0', port = 8050, dev_tools_hot_reload=False)