##AQUI VAMOS A GENERAR NUESTRAS GRÁFICAS
import plotly.express as px
import pandas as pd
from modules.data_processing import cargar_limpiar
#from data_processing import cargar_limpiar ##Para pruebas locales

def plot_satisfaction_vs_payment(df):

    grouped_df = df.groupby(['metodo_pago', 'calificacion_cliente']).size().reset_index(name='conteo')

    fig = px.bar(grouped_df,
                 x = 'conteo',
                 y = 'metodo_pago',
                 color = 'calificacion_cliente',
                 barmode = 'group',
                 title = 'Calificación del Cliente por Método de Pago',
                 range_x = [grouped_df['conteo'].min() - 5, grouped_df['conteo'].max() + 5],
                 )
    
    
    fig.update_layout(xaxis_title='Cantidad de Calificaciones Recibidas',
                      yaxis_title='Método de Pago',
                      legend_title_text='Calificación del Cliente',
                      font=dict(size=12),
                      title_font=dict(size=16)) 
    
    return fig


def main():
    
    df = cargar_limpiar()
    fig = plot_satisfaction_vs_payment(df)
    fig.show()

if __name__ == "__main__":
    main()