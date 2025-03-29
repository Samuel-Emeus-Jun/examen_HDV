##AQUÍ VAMOS A HACER NUESTRO DASHBOARD
import dash
from dash import dcc, html
from modules.data_processing import cargar_limpiar
from modules.plot_gen import plot_satisfaction_vs_payment


app = dash.Dash(__name__)

df = cargar_limpiar()

app.layout = html.Div(childrenn = [
    html.H1("Dashboard de Ventas"),

    html.Div(children = [
        html.H3("Calificación del Cliente por Método de Pago"),
        dcc.Graph(figure = plot_satisfaction_vs_payment(df))
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)




