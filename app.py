import dash
from dash import dcc, html, Input, Output
from modules.data_processing import cargar_limpiar
from modules.plot_gen import plot_satisfaction_vs_payment

# Cargar y limpiar los datos
df = cargar_limpiar()

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
        html.H3("Calificación del Cliente por Método de Pago"),
        dcc.Graph(id='grafico_calificacion_pago',)
    ])
])

@app.callback(
    Output('grafico_calificacion_pago', 'figure'),
    Input('filtro paises', 'value')
)

def actualizar_grafico(pais_seleccionado):
    df_filtrado = df[df['pais'] == pais_seleccionado] if pais_seleccionado else df
    return plot_satisfaction_vs_payment(df_filtrado)


# Ejecutar la app solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    app.run(debug=True)