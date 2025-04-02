##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd

# def cargar():
#     df = pd.read_excel('data/datos_ventas_limpio.xlsx')
#     return df

def cargar_limpiar():

    df = pd.read_excel('data/datos_ventas_limpio.xlsx')

    df = df.dropna()

    ##NADIA



    ##MON

    df['fecha_compra'] = pd.to_datetime(df['fecha_compra'], dayfirst=True)

    # Extraer Año y Mes en formato numérico y texto
    df['Año'] = df['fecha_compra'].dt.year
    df['Mes'] = df['fecha_compra'].dt.strftime('%B')  
    df['Mes_num'] = df['fecha_compra'].dt.month   

    ##ROB



    ##EMM

    df['calificacion_cliente'] = df['calificacion_cliente'].astype(int)
    df['calificacion_cliente'] = df['calificacion_cliente'].astype(str)

    return df
  
    


def main():
    #df = cargar()
    df = cargar_limpiar()
    print(df[df['pais'] == 'Colombia']['total_compra'].sum())  # Imprimir los nombres de las columnas para verificar que se cargaron correctamente


if __name__ == "__main__":
    main()

