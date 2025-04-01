##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd
import numpy as np

def cargar():
    df = pd.read_excel('datos_ventas_limpio.xlsx')
    return df

def analizar_relacion_cantidad_precio(df):
    nuevo_df = df.copy()
    nuevo_df = nuevo_df[['precio_unitario', 'cantidad_comprada']].dropna()

    bins = np.linspace(nuevo_df['precio_unitario'].min(), nuevo_df['precio_unitario'].max(), 15)
    labels = [f"{round(bins[i], 2)} - {round(bins[i+1], 2)}" for i in range(len(bins)-1)]
    nuevo_df['precio_unitario_binned'] = pd.cut(nuevo_df['precio_unitario'], bins=bins, labels=labels, include_lowest=True)

    sorted_labels = sorted(labels, key=lambda x: float(x.split(' - ')[0]))
    nuevo_df['precio_unitario_binned'] = pd.Categorical(nuevo_df['precio_unitario_binned'], categories=sorted_labels, ordered=True)

    return nuevo_df

def main():
    df = cargar()
    df = analizar_relacion_cantidad_precio(df)
    print(df.head())

if __name__ == "__main__":
    main()
