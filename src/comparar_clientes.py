def comparar_clientes(df, opcion):
    '''
    Compara grupos de clientes según el criterio seleccionado.

    Parameters
    ----------
    df : DataFrame

        DataFrame validado con los datos de clientes.

    opcion : str

        Tipo de comparación a realizar.

        Opciones disponibles:

        - "region"
        - "fidelizacion_compra"
        - "fidelizacion_satisfaccion"
        - "promociones"

    Returns
    -------
    analisis : DataFrame

        DataFrame con los resultados de la comparación
        seleccionada.
    '''

    opcion = opcion.lower().strip()

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
