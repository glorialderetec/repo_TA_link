import streamlit as st
import pandas as pd

from src.datos import cargar_dataset, validar_dataset
from src.metricas import obtener_estadisticas_generales
from src.perfiles import crear_cliente_id, Cliente

st.set_page_config(
    page_title="PulseLab Analytics",
    layout="wide"
)

st.title("📊 PulseLab Analytics")

# -------------------
# CARGA DATOS
# -------------------

try:
    df = cargar_dataset()
    df = validar_dataset(df)

except Exception as e:
    st.error(str(e))
    st.stop()

# -------------------
# MENU
# -------------------

opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    [
        "Perfil de cliente",
        "Estadísticas generales",
        "Comparar segmentos",
        "Gráficos"
    ]
)

# -------------------
# PERFIL
# -------------------

if opcion == "Perfil de cliente":

    st.header("Perfil de Cliente")

    id_cliente = st.selectbox(
        "Seleccione un cliente",
        sorted(df["id"].unique())
    )

    cliente = crear_cliente_id(df, id_cliente)

    st.success(cliente.mostrar_resultado())

    st.write("### Datos del cliente")

    st.write({
        "ID": cliente.id,
        "Edad": cliente.age,
        "Ingreso": cliente.income,
        "Frecuencia": cliente.purchase_frequency,
        "Monto compra": cliente.purchase_amount,
        "Satisfacción": cliente.satisfaction_score
    })

# -------------------
# ESTADISTICAS
# -------------------

elif opcion == "Estadísticas generales":

    st.header("Estadísticas Generales")

    metricas = obtener_estadisticas_generales(df)

    st.dataframe(metricas)

# -------------------
# SEGMENTOS
# -------------------

elif opcion == "Comparar segmentos":

    st.header("Comparación de Segmentos")

    criterio = st.selectbox(
        "Seleccione comparación",
        [
            "Compra promedio según región",
            "Compra promedio según fidelización",
            "Satisfacción promedio según fidelización",
            "Compra promedio según promociones"
        ]
    )

    if criterio == "Compra promedio según región":

        analisis = (
            df.groupby("region")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    elif criterio == "Compra promedio según fidelización":

        analisis = (
            df.groupby("loyalty_status")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    elif criterio == "Satisfacción promedio según fidelización":

        analisis = (
            df.groupby("loyalty_status")
            .agg(
                satisfaccion_promedio=("satisfaction_score","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("satisfaccion_promedio", ascending=False)
        )

    else:

        analisis = (
            df.groupby("promotion_usage")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    st.dataframe(analisis)

    st.bar_chart(analisis.iloc[:,0])

# -------------------
# GRAFICOS
# -------------------

elif opcion == "Gráficos":

    st.header("Visualizaciones")

    grafico = st.selectbox(
        "Seleccione gráfico",
        [
            "Compra promedio por fidelización",
            "Distribución de clientes por región"
        ]
    )

    if grafico == "Compra promedio por fidelización":

        datos = (
            df.groupby("loyalty_status")
            ["purchase_amount"]
            .mean()
        )

        st.bar_chart(datos)

    else:

        datos = df["region"].value_counts()

        st.bar_chart(datos)