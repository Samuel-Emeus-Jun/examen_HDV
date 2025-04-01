##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd
import numpy as np

def cargar():
    df = pd.read_excel('data/datos_ventas_limpio.xlsx')
    return df

def analizar_relacion_cantidad_precio(df):
    nuevo_df = df.copy()
    nuevo_df = nuevo_df[['precio_unitario', 'cantidad_comprada']].dropna()

    return nuevo_df

def main():
    df = cargar()
    df = analizar_relacion_cantidad_precio(df)
    print(df.head())

if __name__ == "__main__":
    main()
