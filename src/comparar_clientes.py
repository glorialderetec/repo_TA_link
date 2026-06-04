def comparar_clientes(df):
    '''
    Compara grupos de clientes según el criterio seleccionado.

    Parameters
    ----------
    df : DataFrame

        DataFrame validado con los datos de clientes.

    Returns
    -------
    analisis : DataFrame

        DataFrame con los resultados de la comparación
        seleccionada.
    '''

    print("\nOpciones de comparación:")
    print("1. Compra promedio según región")
    print("2. Compra promedio según fidelización")
    print("3. Satisfacción promedio según fidelización")
    print("4. Compra promedio según uso de promociones")

    opcion = input("\nIngrese una opción: ").lower().strip()

    opciones_validas = [
        "region",
        "fidelizacion_compra",
        "fidelizacion_satisfaccion",
        "promociones"
    ]

    if opcion not in opciones_validas:
        raise ValueError("Opción de comparación inválida.")

    if opcion == "region":

        analisis = df.groupby("region").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    elif opcion == "fidelizacion_compra":

        analisis = df.groupby("loyalty_status").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    elif opcion == "fidelizacion_satisfaccion":

        analisis = df.groupby("loyalty_status").agg(

            satisfaccion_promedio=("satisfaction_score", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "satisfaccion_promedio",
            ascending=False
        )

    elif opcion == "promociones":

        analisis = df.groupby("promotion_usage").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    return analisis
