##AQUÍ VAMOS A HACER NUESTRO DASHBOARD

import dash
import plotly.graph_objects as go
from dash import dcc, html, Input, Output
from modules.data_processing import cargar_limpiar
from modules.plot_gen import plot_satisfaction_vs_payment, plot_cantidad_vs_precio_heatmap, grafica_tendencia_ventas, plot_mapa_interactivo

# Cargar df
df = cargar_limpiar()

#Generar lista de paises
paises_unicos = df['pais'].unique()
paises_unicos = sorted(paises_unicos)
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

        ##CUADRANTE IZQUIERDO
        html.Div(children=[
            html.Div(children=[
                dcc.Graph(id='grafico_1'),
                dcc.Graph(id='grafico_2')
            ], style={'display': 'flex', 'width': '50%', 'justify-content': 'space-between'}),
            html.Div(children=[
                dcc.Graph(id='grafico_3'),
                dcc.Graph(id='grafico_4')
            ], style={'display': 'flex', 'width': '50%', 'justify-content': 'space-between'}),
        ], style={
            'flex': '1',  # Ocupa el 50% sin forzar ancho fijo
            'display': 'flex',
            'flex-direction': 'column',
            'padding-right': '0px',  # Evita que se pegue al mapa
            'box-sizing': 'border-box',
            'overflow': 'hiden'  # Evita que crezca más de lo esperado
        }),

        ## CUADRANTE DERECHO (MAPA)
        html.Div(children=[
            dcc.Graph(id='mapa', style={'width': '100%', 'height': 'auto'})  # Ajusta la altura del mapa
        ], style={
            'flex': '1',  # Ocupa el 50% sin forzar ancho fijo
            'display': 'flex',
            'align-items': 'center',  # Centra el mapa
            'justify-content': 'center',
            'overflow': 'hidden'  # Evita que desborde
        })

    ], style={'display': 'flex', 'width': '100%', 'height': '80vh'})  # Contenedor general
])



##APLICACIÓN DE FILTROS EN LOS GRÁFICOS

# Placeholder para los gráficos que no se están utilizando en este momento
fig_placeholder = go.Figure()

@app.callback(
    [Output('grafico_1', 'figure'),
     Output('grafico_2', 'figure'),
     Output('grafico_3', 'figure'),
     Output('grafico_4', 'figure'),
     Output('mapa', 'figure')],
    Input('filtro paises', 'value')
)


def actualizar_grafico(pais_seleccionado):
    df_filtrado = df[df['pais'] == pais_seleccionado] if pais_seleccionado else df

    fig_1 = grafica_tendencia_ventas(df_filtrado)
    fig_2 = grafica_tendencia_ventas(df_filtrado)
    fig_3 = plot_cantidad_vs_precio_heatmap(df_filtrado)
    fig_4 = plot_satisfaction_vs_payment(df_filtrado)
    fig_5 = plot_mapa_interactivo(df_filtrado)

    return fig_1, fig_2, fig_3, fig_4, fig_5


if __name__ == "__main__":
    app.run(debug=True)