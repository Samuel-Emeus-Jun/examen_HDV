import dash
from dash import dcc, html
from modules.data_processing import cargar_limpiar
from modules.plot_gen import plot_satisfaction_vs_payment

# Cargar y limpiar los datos
df = cargar_limpiar()

# Crear la app de Dash
app = dash.Dash(__name__)

# Estructura del Layout
app.layout = html.Div(children=[
    html.H1("Dashboard de Ventas"),
    html.Div(children=[
        html.H3("Calificación del Cliente por Método de Pago"),
        dcc.Graph(figure=plot_satisfaction_vs_payment(df))
    ])
])

# Ejecutar la app solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    app.run(debug=True)