##AQUI VAMOS A CARGAR EL ARCHIVO Y HACER LA LIMPIEZA GENERAL
import pandas as pd

def cargar_limpiar():
    df = pd.read_excel('data/datos_ventas_limpio.xlsx')

    df['calificacion_cliente'] = pd.to_numeric(df['calificacion_cliente'], errors='coerce')
    #df['metodo_pago'] = df['metodo_pago'].astype('category')
    
    df = df.dropna(subset = ['calificacion_cliente' , 'metodo_pago'])

    return df
  
    


def main():
    df = cargar_limpiar()
    print(df.head())


if __name__ == "__main__":
    main()

