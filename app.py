##AQUÍ VAMOS A HACER NUESTRO DASHBOARD

import dash
import plotly.graph_objects as go
from dash import dcc, html, Input, Output
from modules.data_processing import cargar_limpiar
from modules.plot_gen import plot_satisfaction_vs_payment

# Cargar df
df = cargar_limpiar()

#Limpieza de df por gráfica

#df = limpiar_satisfaccion_cliente(df)

##CREO QUE SI VAMOS A TENER QUE UNIFICAR LA LIMPIEZA :(



#Generar lista de paises
paises_unicos = df['pais'].dropna().unique()
opciones_paises = [{'label' : pais, 'value': pais} for pais in paises_unicos]

# Crear la app de Dash
app = dash.Dash(__name__)

# Estructura del Layout
app.layout = html.Div(children=[
    html.H1("Dashboard de Ventas"),

    dcc.Dropdown(
        id = 'filtro paises',
        options = opciones_paises,
        placeholder = 'Selecciona un país',
        clearable = True,
    ),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id= 'grafico_1',),
            dcc.Graph(id = 'grafico_2')
        ], style={'display': 'flex', 'width' : '100%', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        html.Div(children=[
            dcc.Graph(id = 'grafico_3'),
            dcc.Graph(id = 'grafico_4')
        ], style={'display': 'flex', 'width' : '100%', 'flex-direction': 'row', 'justify-content': 'space-between'}),
    ])
])

##APLICACIÓN DE FILTROS EN LOS GRÁFICOS

# Placeholder para los gráficos que no se están utilizando en este momento
fig_placeholder = go.Figure()

@app.callback(
    [Output('grafico_1', 'figure'),
     Output('grafico_2', 'figure'),
     Output('grafico_3', 'figure'),
     Output('grafico_4', 'figure')],
    Input('filtro paises', 'value')
)


def actualizar_grafico(pais_seleccionado):
    df_filtrado = df[df['pais'] == pais_seleccionado] if pais_seleccionado else df

    fig_1 = fig_placeholder
    fig_2 = fig_placeholder
    fig_3 = fig_placeholder
    fig_4 = plot_satisfaction_vs_payment(df_filtrado)

    return fig_1, fig_2, fig_3, fig_4


if __name__ == "__main__":
    app.run(debug=True)