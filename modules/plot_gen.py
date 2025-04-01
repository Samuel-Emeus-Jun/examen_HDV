##AQUI VAMOS A GENERAR NUESTRAS GRÁFICAS
import plotly.express as px
import pandas as pd
import numpy as np
from data_processing import cargar, analizar_relacion_cantidad_precio
# from data_processing import cargar  ## Para pruebas locales

def plot_cantidad_vs_precio(df):
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

def main():
    df = cargar()
    df = analizar_relacion_cantidad_precio(df)  # Limpieza antes del análisis
    fig = plot_cantidad_vs_precio(df)
    fig.show()

if __name__ == "__main__":
    main()
