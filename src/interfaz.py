def mostrar_menu():
  '''
    Función que muestra el menu de opciones al usuario
    Parameters
    None
    Returns
    None
    '''
  print("MENU DE OPCIONES:\n1.⁠ ⁠Consultar perfil de cliente\n2.⁠ ⁠Mostrar estadísticas generales\n3.⁠ ⁠Comparar segmentos\n4.⁠ ⁠Mostrar gráficos\n5.⁠ ⁠Generar recomendaciones\n6.⁠ ⁠Salir\n")
  
def pedir_opcion():
    '''
    Función que solicita al usuario una opción del menú y valida
    que sea un número entero entre 1 y 6.

    Returns
    -------
    opcion : int
        Opción válida elegida por el usuario.
    '''

    while True:

        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion < 1 or opcion > 6:
              print("Error: debe ingresar una opción entre 1 y 6.")
              continue

            return opcion

        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue
