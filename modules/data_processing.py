##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd

def limpieza_tendencia_ventas():
    df = pd.read_excel('data/datos_ventas_limpio.xlsx')
    df_tendencia_ventas = df.copy()

    # Convertir la columna de fecha a tipo datetime
    df_tendencia_ventas['fecha_compra'] = pd.to_datetime(df_tendencia_ventas['fecha_compra'], dayfirst=True)

    # Extraer Año y Mes en formato numérico y texto
    df_tendencia_ventas['Año'] = df_tendencia_ventas['fecha_compra'].dt.year
    df_tendencia_ventas['Mes'] = df_tendencia_ventas['fecha_compra'].dt.strftime('%B')  
    df_tendencia_ventas['Mes_num'] = df_tendencia_ventas['fecha_compra'].dt.month       

    # Eliminar filas con valores nulos en columnas clave
    df_tendencia_ventas = df_tendencia_ventas.dropna(subset=['total_compra', 'categoria_producto'])

    # Agrupar ventas por Año, Mes y Categoría
    ventas_tiempo_categoria = df_tendencia_ventas.groupby(['Año', 'Mes', 'Mes_num', 'categoria_producto'])['total_compra'].sum().reset_index()

    # Ordenar los datos por Año y Mes_num
    ventas_tiempo_categoria = ventas_tiempo_categoria.sort_values(['Año', 'Mes_num'])

    # Crear una columna combinada Año-Mes para el eje X
    ventas_tiempo_categoria['Año_Mes'] = ventas_tiempo_categoria['Año'].astype(str) + " " + ventas_tiempo_categoria['Mes']

    return ventas_tiempo_categoria



