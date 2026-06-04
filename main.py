# MAIN
from src.datos import (cargar_dataset, validar_dataset)
from src.interfaz import(mostrar_menu, pedir_opcion)
from src.interfaz import pedir_id_cliente
from src.perfiles import Cliente
from src.metricas import obtener_estadisticas_generales
from src.graficos import mostrar_menu_graficos
from tabulate import tabulate

try:
    df = cargar_dataset()
    df_valido = validar_dataset(df)

except Exception as e:
    print(e)
    
    quit() #SUPER A CHEQUEAR


while True:
    mostrar_menu()
    opcion = pedir_opcion()
    
    if opcion == 1:

        id_cliente = pedir_id_cliente(df_valido)

        fila = df_valido[df_valido["id"] == id_cliente]

        cliente = Cliente(
            fila["id"].iloc[0],
            fila["age"].iloc[0],
            fila["income"].iloc[0],
            fila["purchase_frequency"].iloc[0],
            fila["purchase_amount"].iloc[0],
            fila["satisfaction_score"].iloc[0]
        )

        print("\nPerfil del cliente:")
        print(cliente.clasificar_perfil())

    elif opcion == 2:

        df_metricas = obtener_estadisticas_generales(df_valido)
        
        print("\nESTADÍSTICAS GENERALES")
        print(tabulate(df_metricas, headers='keys', tablefmt='grid', showindex=False))

    elif opcion == 3:

        print("Comparando segmentos...")

    elif opcion == 4:

        mostrar_menu_graficos(df_valido)

    elif opcion == 5:

        print("Generando recomendaciones...")

    elif opcion == 6:

        print("Programa finalizado.")
        break
    
    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()

    if continuar != "s":
        print("Programa finalizado.")
        break
