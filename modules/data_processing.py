##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
#Se realizaron los siguientes cambios
# Borrar comentarios
# Normalizar nombres de columnas
# Corregir valores que parecen fechas en "precio_unitario"
# Limpiar y convertir la columna de precio_unitario
# Rellenar valores nulos en 'precio_unitario' con la media por producto y país
# Convertir otras columnas numéricas
# Formatear la columna de fecha
# Calcular total de compra
# Retorna el DataFrame modificado

import pandas as pd
from datetime import datetime

def limpiar_datos_ventas(df):
    df = df.drop(columns=['Comentarios'], errors='ignore')
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    def corregir_precio_unitario(valor):
        if isinstance(valor, datetime):
            return valor.strftime('%d.%m')
        return valor

    if 'precio_unitario' in df.columns:
        df['precio_unitario'] = df['precio_unitario'].apply(corregir_precio_unitario)
        df['precio_unitario'] = df['precio_unitario'].astype(str).str.replace(",", ".", regex=True)
        df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')

    if 'producto' in df.columns and 'pais' in df.columns and 'precio_unitario' in df.columns:
        df['precio_unitario'] = df.groupby(['producto', 'pais'])['precio_unitario'].transform(lambda x: x.fillna(x.mean()))

    columnas_numericas = ['cantidad_comprada', 'precio_unitario', 'total_compra']
    for col in columnas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'fecha_compra' in df.columns:
        df['fecha_compra'] = pd.to_datetime(df['fecha_compra'], errors='coerce').dt.strftime('%d/%m/%Y')

    if 'cantidad_comprada' in df.columns and 'precio_unitario' in df.columns:
        df['total_compra'] = df['cantidad_comprada'] * df['precio_unitario']
    
    return df

df = pd.read_excel('datos_ventas.xlsx')
df_limpio = limpiar_datos_ventas(df)
ruta_guardado = "datos_ventas_limpio.xlsx"
df_limpio.to_excel(ruta_guardado, index=False)
print(f"\nArchivo limpio guardado en: {ruta_guardado}")

