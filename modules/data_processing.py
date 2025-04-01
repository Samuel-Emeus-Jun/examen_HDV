##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd

def cargar():
    df = pd.read_excel('data/datos_ventas_limpio.xlsx')
    return df

def limpiar_satisfaccion_cliente(df):

    nuevo_df = df.copy()
    #df = pd.read_excel('data/datos_ventas_limpio.xlsx')

    #df['calificacion_cliente'] = df['calificacion_cliente'].astype(str)
    #df['metodo_pago'] = df['metodo_pago'].astype('category')
    
    nuevo_df = nuevo_df.dropna(subset = ['calificacion_cliente' , 'metodo_pago'])
    nuevo_df['calificacion_cliente'] = nuevo_df['calificacion_cliente'].astype(int)
    nuevo_df['calificacion_cliente'] = nuevo_df['calificacion_cliente'].astype(str)

    return nuevo_df
  
    


def main():
    df = cargar()
    df = limpiar_satisfaccion_cliente(df)
    print(df.head())


if __name__ == "__main__":
    main()

