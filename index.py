import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_loading_spinners as dls
from app import app
from app import server
import functools
from apps import steam, settings, fuel, efficiency, home, about
import dash_dangerously_set_inner_html

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "Buencafé Dashboard"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='wrapper-top',children = [
        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <div class="menu-wrap">
            <input type="checkbox" class="toggler" />
            <div class="hamburger"><div></div></div>
            <div class="menu">
                <div>
                <div>
                    <ul>
                    <li><i class="fas fa-house-user"></i><a href="/apps/home">Home</a></li>
                    <li><i class="fas fa-faucet"></i><a href="/apps/steam">Steam</a></li>
                    <li><i class="fas fa-gas-pump"></i><a href="/apps/fuel">Fuel</a></li>
                    <li><i class="fas fa-percentage"></i><a href="/apps/efficiency">Efficiency</a></li>
                    <li><i class="far fa-address-card"></i><a href="/apps/aboutus">About Us</a></li>
                    </ul>
                </div>
                </div>
            </div>
            </div>
        '''),

        
        html.Div(id='page-content', className = 'content-class', children = []),
        
    ])
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

    if pathname == '/apps/steam':
        return steam.layout
    elif pathname == '/apps/home' or pathname == '/':
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
    app.run_server(debug=True,dev_tools_hot_reload=True)
    #app.run_server(debug=True, host ='0.0.0.0', port = 8050, dev_tools_hot_reload=False)