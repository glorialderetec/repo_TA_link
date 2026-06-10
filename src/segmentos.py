def segmentos(df):
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
    
    while True: 
        opcion = input("\nIngrese una opción: ").lower().strip()
        if opcion not in ['1', '2', '3', '4']:
            raise ValueError("Opción de comparación inválida.")
        else:
            break

    if opcion == '1':

        analisis = df.groupby("region").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    elif opcion == '2':

        analisis = df.groupby("loyalty_status").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    elif opcion == '3':

        analisis = df.groupby("loyalty_status").agg(

            satisfaccion_promedio=("satisfaction_score", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "satisfaccion_promedio",
            ascending=False
        )

    elif opcion == '4':

        analisis = df.groupby("promotion_usage").agg(

            compra_promedio=("purchase_amount", "mean"),

            cantidad_clientes=("id", "count")

        )

        analisis = analisis.sort_values(
            "compra_promedio",
            ascending=False
        )

    return analisis
