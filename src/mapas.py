import folium
from folium.plugins import HeatMap

def generar_mapa_regiones(df):
    '''
    Genera un mapa de calor interactivo utilizando Folium a partir de la
    distribución geográfica de los clientes según su región.

    La función asigna coordenadas representativas a cada región
    ("North", "South", "East" y "West"), calcula la cantidad de clientes
    presentes en cada una y construye un mapa de calor donde la intensidad
    del color refleja la concentración de registros.

    El mapa generado se guarda en un archivo HTML que puede visualizarse
    posteriormente en cualquier navegador web.

    Parameters
    ----------
    df : DataFrame
        DataFrame validado con los datos de los clientes. Debe contener,
        como mínimo, la columna "region" con valores pertenecientes a las
        categorías "North", "South", "East" y "West".

    Raises
    ------
    KeyError
        Si la columna "region" no existe en el DataFrame o contiene
        regiones sin coordenadas asociadas.

    Returns
    -------
    None.
        La función no retorna ningún valor. Como resultado genera y guarda
        un archivo HTML con el mapa de calor interactivo.

    '''
    #Defino coordenadas
    coordenadas = {

        "North": (45,-95),

        "South": (30,-95),

        "East": (40,-75),

        "West": (40,-120)

    }

    
    df = df.copy()

    #Convertir regiones en coordenadas
    df["lat"] = df["region"].map(
        lambda x: coordenadas[x][0]
    )

    df["lon"] = df["region"].map(
        lambda x: coordenadas[x][1]
    )
    
    #Contar clientes por región
    conteo = df.groupby(
        ["lat","lon"]
    ).size().reset_index(name="cantidad")
    
    #Crear el mapa
    mapa = folium.Map(

        location=[38,-97],

        zoom_start=4

    )
    #Agregar el HeatMap
    HeatMap(

        conteo.values.tolist(),

        radius=40,

        blur=25

    ).add_to(mapa)
    
    #Guardar el mapa
    mapa.save("mapa_clientes.html")

    print("Mapa generado correctamente.")
    
    
    
