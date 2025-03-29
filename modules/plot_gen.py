##AQUI VAMOS A GENERAR NUESTRAS GRÁFICAS
import plotly.express as px
import pandas as pd
from data_processing import cargar_limpiar

def plot_satisfaction_vs_payment(df):
    fig = px.bar(df,
                 x = 'metodo_pago',
                 y = 'calificacion_cliente',
                 color = 'metodo_pago',
                 barmode = 'group',
                 title = 'Calificación del Cliente por Método de Pago',)
    
    fig.update_layout(xaxis_title='Método de Pago',
                      yaxis_title='Calificación del Cliente',
                      legend_title_text='Método de Pago',
                      font=dict(size=12),
                      title_font=dict(size=16)) 
    
    return fig


def main():
    
    df = cargar_limpiar()
    fig = plot_satisfaction_vs_payment(df)
    fig.show()

if __name__ == "__main__":
    main()