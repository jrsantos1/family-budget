import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html

class utils:

    @classmethod
    def row(cls, children: list, altura, id = ''):
        return dbc.Row(children=children, style={'height': str(altura) + 'vh'}, id=id)

    @classmethod
    def drop_down_group(cls, label: str, id_dropdown, md, options={}):
        return dbc.Col(children=[
            html.Label(children=label),
            dcc.Dropdown(id=id_dropdown, options=options)
        ], md=md)

    @classmethod
    def data_picker(cls, label: str, id_data_picker, md):
        return dbc.Col(children=[
            html.Label(children=label),
            dcc.DatePickerSingle(id=id_data_picker, className='w-100')
        ], md=md, className='d-flex flex-column')
    @classmethod
    def input(cls,label, id_input, md):
        return dbc.Col(children=[
            html.Label(children=label),
            dbc.Input(type='number', id=id_input)
        ], md=md)