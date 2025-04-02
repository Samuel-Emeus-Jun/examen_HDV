##AQUI VAMOS A GENERAR NUESTRAS GRÁFICAS
import plotly.express as px
import pandas as pd
import numpy as np
#from modules.data_processing import cargar_limpiar
from data_processing import cargar_limpiar ##Para pruebas locales


##NADIA

def plot_cantidad_vs_precio_heatmap(df):

    bins = np.linspace(df['precio_unitario'].min(), df['precio_unitario'].max(), 15)
    labels = [f"{round(bins[i], 2)} - {round(bins[i+1], 2)}" for i in range(len(bins)-1)]
    df['precio_unitario_binned'] = pd.cut(df['precio_unitario'], bins=bins, labels=labels, include_lowest=True)

    sorted_labels = sorted(labels, key=lambda x: float(x.split(' - ')[0]))
    df['precio_unitario_binned'] = pd.Categorical(df['precio_unitario_binned'], categories=sorted_labels, ordered=True)   

    fig = px.density_heatmap(
        df,
        x="precio_unitario_binned",
        y="cantidad_comprada",
        color_continuous_scale="Blues",
        labels={"precio_unitario_binned": "Precio Unitario (Agrupado)", "cantidad_comprada": "Cantidad Comprada"},
        title="Mapa de Calor: Relación entre Cantidad Comprada y Precio Unitario"
    )

    fig.update_xaxes(categoryorder='array', categoryarray=sorted_labels)
    
    return fig


##MON

def grafica_tendencia_ventas(df):
    """
    Genera un gráfico de línea para visualizar la tendencia de ventas a lo largo del tiempo.
    """

    df = df.groupby(['Año', 'Mes', 'Mes_num', 'categoria_producto'])['total_compra'].sum().reset_index()

    # Ordenar los datos por Año y Mes_num
    df = df.sort_values(['Año', 'Mes_num'])

    # Crear una columna combinada Año-Mes para el eje X
    df['Año_Mes'] = df['Año'].astype(str) + " " + df['Mes']

    fig = px.line(
        df,
        x="Año_Mes",
        y="total_compra",
        color="categoria_producto",
        markers=True,
        title="Tendencia de Ventas en el Tiempo",
        labels={"total_compra": "Ventas Totales", "Año_Mes": "Año y Mes"},
        category_orders={"Año_Mes": df['Año_Mes'].unique().tolist()}
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


##ROB


##EM

def plot_satisfaction_vs_payment(df):

    grouped_df = df.groupby(['metodo_pago', 'calificacion_cliente']).size().reset_index(name='conteo')

    fig = px.bar(grouped_df,
                 x = 'conteo',
                 y = 'metodo_pago',
                 color = 'calificacion_cliente',
                 barmode = 'group',
                 title = 'Calificación del Cliente por Método de Pago',
                 range_x = [grouped_df['conteo'].min(), grouped_df['conteo'].max() + 5],
                 color_discrete_map = {  
                    '1': 'palevioletred',
                    '2': 'tomato',
                    '3': 'sandybrown',
                    '4': 'lightgreen',
                    '5': 'dodgerblue'
                 }
                 )
    
    
    fig.update_layout(xaxis_title='Cantidad de Calificaciones Recibidas',
                      yaxis_title='Método de Pago',
                      legend_title_text='Calificación del Cliente',
                      font=dict(size=12),
                      title_font=dict(size=16)) 
    
    return fig


def pie_status(df):
    """
    Genera un gráfico de pastel para visualizar la distribución de estados de envío.
    """

    df_agrupado = df.groupby('estado_envio').size().reset_index(name='conteo')

    fig = px.pie(df_agrupado, 
                 values='conteo', 
                 names='estado_envio',
                 color='estado_envio',
                 title='Distribución de Estados de Envío',
                 color_discrete_map={
                     'Entregado': 'springgreen',
                     'Enviado': 'deepskyblue',
                     'Cancelado': 'orangered',
                     'Pendiente': 'plum',
                 })

    fig.update_traces(textinfo='percent+label')

    return fig


def plot_mapa_interactivo(df):

    df_agrupado = df.groupby('pais', as_index=False)['total_compra'].sum()

    fig = px.choropleth(df_agrupado,
                    locations = 'pais',
                    locationmode = 'country names',
                    color = 'total_compra',
                    hover_name = 'pais',
                    hover_data = ['total_compra'],
                    color_continuous_scale = 'Viridis',
                    title = 'Mapa Interactivo de Ventas por País',
    )

    return fig


def main():
    
    df = cargar_limpiar()
    # print(df['estado_envio'].unique())
    # print(df['estado_envio'].value_counts())
    fig = pie_status(df)
    fig.show()

if __name__ == "__main__":
    main()