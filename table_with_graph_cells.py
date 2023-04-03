import dash
import dash_html_components as html
import dash_table
import pandas as pd

# criar um DataFrame de exemplo
df = pd.DataFrame({
    'Ativo': ['AAPL', 'AMZN', 'GOOG', 'NFLX'],
    'Retorno': [0.05, -0.03, 0.02, 0.08]
})

# criar a app
app = dash.Dash(__name__)

# definir a função de renderização da coluna
def render_retorno_com_barra(valor):
    estilo = {'width': str(abs(valor)*100)+'%', 'height': '20px', 'margin': 'auto'}
    if valor >= 0:
        cor = 'bg-success'
    else:
        cor = 'bg-danger'
    return html.Div(
        [
            html.Div(f"{valor:.0%}", style={'float': 'right'}),
            html.Div(
                className='progress',
                children=[
                    html.Div(className=f"progress-bar {cor}", style=estilo)
                ]
            )
        ]
    )

# definir a tabela
app.layout = dash_table.DataTable(
    id='tabela',
    columns=[
        {'name': 'Ativo', 'id': 'Ativo'},
        {'name': 'Retorno', 'id': 'Retorno', 'type': 'numeric', 'format': '.2%', 'presentation': 'div', 'render': render_retorno_com_barra}
    ],
    data=df.to_dict('records'),
    style_data_conditional=[
        {
            'if': {'column_id': 'Retorno'},
            'textAlign': 'center'
        }
    ],
    style_cell={
        'minWidth': '0px',
        'maxWidth': '100px',
        'whiteSpace': 'normal'
    },
    style_cell_conditional=[
        {
            'if': {'column_id': 'Retorno'},
            'width': '20%'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white',
        'fontWeight': 'bold'
    },
)

# executar a app
if __name__ == '__main__':
    app.run_server(debug=True)
