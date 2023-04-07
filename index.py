from cgitb import html

from config import *
from dash import html
from dash.dependencies import Input, Output
from dash import dcc

from components import relatorio, extrato, sidebar

content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2, style={'backgroundColor': 'rgba(0, 0, 0, 0.78)','height': '100vh'}),
        dbc.Col([
            content
        ], md=10)
    ], style={})
], fluid=True)

@app.callback(Output(component_id='page-content', component_property='children'),
              Input(component_id='url', component_property='pathname'))
def render_page(pathname):
    if pathname == '/' or pathname == '/relatorio':
        return relatorio.layout
    else:
        return extrato.layout

if __name__ == '__main__':
    app.run(port=8051, debug=True)