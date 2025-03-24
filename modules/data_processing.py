#importar librerías
import pandas as pd
#crear Dataframe con todo el archivo .csv
df_original=pd.read_excel('data/datos_ventas.xlsx')
"""
#creae sub-DataFrame con las columnas de interés
df_mocho=df.iloc[:, 4:10]

#Preguntar datos de interés
columna=input("Nombre de columna: ")
registro=input("Nombre de registro: ")
#Mostrar columnas de interés
print(df_mocho[df_mocho[columna]==registro])
print(f"Cantidad de registros encontrados: {len(df[df[columna]==registro])}")
"""
#Mostrar Cantidad de datos diferentes en cada columna
def Mostrar_Datos_Dif(df):
    print("*****VALORES DIFERENTES DE LAS CATEGORIAS*****")
    print(f"ID: {len(df["ID_Transaccion"].unique())}")
    print(f"Nombres de clientes: {len(df["Nombre_Cliente"].unique())}")
    print(f"Correos electrónicos: {len(df["Correo_Electronico"].unique())}")
    print(f"Paises: {len(df["Pais"].unique())}")
    print(f"Categorias de producto: {len(df["Categoria_Producto"].unique())}")
    print(f"Productos: {len(df["Producto"].unique())}")
    print(f"Cantidad comprada: {len(df["Cantidad_Comprada"].unique())}")
    print(f"Precios unitarios: {len(df["Precio_Unitario"].unique())}")
    print(f"Totales de compra: {len(df["Total_Compra"].unique())}")
    print(f"Métodos de pago: {len(df["Metodo_Pago"].unique())}")
    print(f"Estados de envío: {len(df["Estado_Envio"].unique())}")
    #print(f"{df["Pais"].unique()}")

#Crear anuevo dataframe con los nombres de clientes repetidos y su frecuencia
def Datos_Nombres_Repetidos(df):
    Nombres_Repetidos = df['Nombre_Cliente'].value_counts()
    Nombres_Repetidos = Nombres_Repetidos[Nombres_Repetidos > 1].reset_index()
    Nombres_Repetidos.columns = ['Nombre_Cliente', 'Frecuencia']
    return Nombres_Repetidos
Nombres_Repetidos=Datos_Nombres_Repetidos(df_original)
Nombres_Repetidos=Nombres_Repetidos[Nombres_Repetidos['Frecuencia']>3]

def Contar_Paises(df):
    Paises = df['Pais'].value_counts()
    Paises = Paises.reset_index()
    Paises.columns = ['Pais', 'Frecuencia']
    return Paises
Paises=Contar_Paises(df_original)

#print(f"Total de nombres repetidos: {Nombres_Repetidos['Frecuencia'].sum()}")
#son 10,000 registros y 9434 nombres únicos por lo que se espera que haya 566 nombres repetidos
#la última linea solo es una comprobación de que cuadren los números
#Muestra 1039 como resultado, pero al restarle los 473 registros del dataframe "Nombres_Repetidos", da 566

#print(f"Top 10 nombres repetidos: \n{Nombres_Repetidos[Nombres_Repetidos['Frecuencia']>3]}")

Mostrar_Datos_Dif(df_original)
print(Nombres_Repetidos)
print(Paises)