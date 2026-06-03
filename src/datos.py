# DATOS
import os
import pandas as pd

def cargar_dataset():
    '''
    funcion que carga el dataset y lo convierte en un DataFrame

    Returns
    -------
    df : DataFrame
        DataFrame con los datos del dataset.

    '''
    try:
        ruta_proyecto = "C:\\Users\\Usuario\\Documents\\GitHub\\repo_TA\\"
        os.chdir(ruta_proyecto)
        
        df = pd.read_csv('src\\data\\customer_data.csv')
        
        return df
    
    except FileNotFoundError:
        return None
        
    
def validar_dataset(df):
    '''
    función que valida que el dataset no esté vacío, que tengas las columnas necesarias y que las columnas con datos numericos contengan datos de tipo int.
    además, levanta un mensaje de error si no se pudo encontrar el dataset

    Parameters
    ----------
    df : DataFrame
        DataFrame con los datos del dataset.
        con las siguientes columnas: ["id","age","gender","income","education","region","loyalty_status","purchase_frequency","purchase_amount","product_category","promotion_usage","satisfaction_score"]

    Raises
    ------
    ValueError
        si no se encontró el dataset en la funcion cargar_dataset, si el dataframe esta vacío, si faltan columnas o si las columnas con datos numericos no tienen datos tipo int.

    Returns
    -------
    None.

    '''
    
    if df is None:
        raise ValueError('Error: no se encontró el archivo customer_data.csv')
    
    if df.empty:
        raise ValueError("Error: el dataset está vacío")
    
    columnas_necesarias = ["id","age","gender","income","education","region","loyalty_status","purchase_frequency","purchase_amount","product_category","promotion_usage","satisfaction_score"]
    
    for columna in columnas_necesarias:
        if columna not in df.columns:
            raise ValueError(f'Error: falta la columna {columna}')
   # esto de aca abajo es muy a chequear, tal vez lo podemos poner en el docstring y ni validarlo     
    columnas_numericas = ["id", "age", "income", "purchase_amount", "promotion_usage", "satisfaction_score"]
    
    for columna in columnas_numericas:
        try:
            pd.to_numeric(df[columna])
            
        except ValueError:
            raise ValueError(f'Error: la columna {columna} contiene valores no numericos')
    
    num_filas_originales = len(df)
    
    df = df.dropna()
    
    filas_eliminadas = num_filas_originales - len(df)
    
    if filas_eliminadas > 0:
        print(f'Se eliminaron {filas_eliminadas} filas con datos faltantes')
    
    return df