##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd

def cargar_limpiar():
    df = pd.read_excel('data/datos_ventas_limpio.xlsx')

    #df['calificacion_cliente'] = df['calificacion_cliente'].astype(str)
    #df['metodo_pago'] = df['metodo_pago'].astype('category')

    
    df = df.dropna(subset = ['calificacion_cliente' , 'metodo_pago'])
    df['calificacion_cliente'] = df['calificacion_cliente'].astype(int)
    df['calificacion_cliente'] = df['calificacion_cliente'].astype(str)

    return df
  
    


def main():
    df = cargar_limpiar()
    print(df.head())


if __name__ == "__main__":
    main()

