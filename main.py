# MAIN
from src.datos import (cargar_dataset, validar_dataset)
from src.interfaz import(mostrar_menu, pedir_opcion, pedir_id_cliente)
from src.perfiles import crear_cliente_id
from src.metricas import obtener_estadisticas_generales
from src.graficos import mostrar_menu_graficos
from src.segmentos import segmentos
from src.recomendaciones_api import generar_recomendacion_api
from rich.console import Console
from rich.table import Table
#from tabulate import tabulate

try:
    df = cargar_dataset()
    df_valido = validar_dataset(df)

except Exception as e:
    print(e)
    
    quit() 


while True:
    mostrar_menu()
    opcion = pedir_opcion()
    
    if opcion == 1:

        id_cliente = pedir_id_cliente(df_valido)

        cliente= crear_cliente_id(df_valido, id_cliente)

        print("\nPerfil del cliente:")
        print(cliente.mostrar_resultado())

    elif opcion == 2:

        df_metricas = obtener_estadisticas_generales(df_valido)
        
        #print("\nESTADÍSTICAS GENERALES")
        #print(tabulate(df_metricas, headers='keys', tablefmt='grid', showindex=False))
        
        console = Console()
        
        tabla = Table(title="\nEstadísticas Generales")
        
        tabla.add_column("Métrica")
        tabla.add_column("Valor")
        
        for columna in df_metricas.columns:
            tabla.add_row(columna,str(df_metricas[columna][0]))
        
        console.print(tabla)

    elif opcion == 3:

        print("Comparando segmentos...")
        analisis = segmentos(df)
       
        console = Console()

        def mostrar_dataframe(df, titulo="Tabla"):
            tabla = Table(title=titulo)

            for columna in df.columns:
                tabla.add_column(str(columna))

            for _, fila in df.iterrows():
                tabla.add_row(*[str(valor) for valor in fila])

            console.print(tabla)
            
        mostrar_dataframe(analisis.reset_index(),"\nComparación de segmentos")

    elif opcion == 4:

        mostrar_menu_graficos(df_valido)

    elif opcion == 5:
        id_cliente = pedir_id_cliente(df_valido)

        cliente= crear_cliente_id(df_valido, id_cliente)

        print("Generando recomendaciones...")
        reco = generar_recomendacion_api(cliente)
        print(reco)
    elif opcion==6:
        link= "http://localhost:8501"
        print(link)
    
    elif opcion == 7:
        
        print("Programa finalizado.")
        break
    
    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()

    if continuar != "s":
        print("Programa finalizado.")
        break
