##AQUI VAMOS A GENERAR NUESTRAS GRÁFICAS
import plotly.express as px
import pandas as pd
from data_processing import limpieza_tendencia_ventas    

def grafica_tendencia_ventas(df_tendencia_ventas):
    """
    Genera un gráfico de línea para visualizar la tendencia de ventas a lo largo del tiempo.
    """
    fig = px.line(
        df_tendencia_ventas,
        x="Año_Mes",
        y="total_compra",
        color="categoria_producto",
        markers=True,
        title="Tendencia de Ventas en el Tiempo",
        labels={"total_compra": "Ventas Totales", "Año_Mes": "Año y Mes"},
        category_orders={"Año_Mes": df_tendencia_ventas['Año_Mes'].unique().tolist()}
    )

    fig.update_layout(
        xaxis_title='Año y Mes',
        yaxis_title='Ventas Totales',
        legend_title_text='Categoría del Producto',
        font=dict(size=12),
        title_font=dict(size=16),
        xaxis=dict(tickangle=-45)  
    )

    return fig

