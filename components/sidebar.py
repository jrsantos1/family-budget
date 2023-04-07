from builtins import id

import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output, State
from config import app
from dash.exceptions import PreventUpdate
from bll import bll

from components.utils import utils

layout = dbc.Container(children=[
    dbc.Col(children=[
        utils.row(children=[
            dbc.Nav([
                dbc.NavLink(children="Relatório", href="/relatorio", active="exact", className='bg-sucess'),
                dbc.NavLink(children="Extrato", href="/extrato", active="exact")
            ], className='d-flex align-items-center')
        ], altura=33),
        utils.row(children=[
            dbc.Col([
                dbc.Button("Novo gasto", outline=True, color="primary", className="me-1 w-100", id='btn_nova_despesa'),
            ], className='d-flex align-items-center')
        ], altura=33),
        dbc.Modal(children=[
            dbc.ModalHeader([
                dbc.ModalTitle(children="Nova Despesa"),
            ]),
            dbc.ModalBody(children=[
                dbc.Col([
                    dbc.Row([
                        utils.data_picker(label='Data Gasto', md=2, id_data_picker='data_gasto_id'),
                        utils.drop_down_group(id_dropdown='membro_id', label='Membro', md=3, options=bll.getIngrantes()),
                        utils.drop_down_group(id_dropdown='categoria_id', label='Categoria Gasto', md=3, options=bll.getCategorias()),
                        utils.drop_down_group(id_dropdown='sub_categoria_id', label='Sub Categoria', md=2),
                        utils.input(id_input='valor_id', label='Valor', md=2)
                    ]),
                ], md=12),
                html.Hr(),
                dbc.Button("Inserir", outline=True, color="primary", className="me-1 w-100", id='btn_inserir_gasto_id')

            ])
        ], is_open=False, id='modal_nova_despesa', size="xl")

    ])
])

@app.callback(Output('modal_nova_despesa', 'is_open'),
              Input('btn_nova_despesa', 'n_clicks'),
              State('modal_nova_despesa', 'is_open'))
def nova_despesa(clique, estado):
    if clique:
        return not estado

@app.callback(Output('sub_categoria_id', 'options'),
              Input('categoria_id', 'value'))
def get_sub_categoria(value):
    if value == None:
        raise PreventUpdate
    return bll.getSubCategoriaByCategoryId(value)
