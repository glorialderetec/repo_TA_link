import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.graficos import (
    grafico_ingreso_vs_compra,
    grafico_distribucion_perfiles
)

# Config
st.set_page_config(page_title="Sistema de Clientes", layout="wide")

st.title("📊 Sistema de Análisis y Perfilado de Clientes")

# Cargar datos
df = pd.read_csv("data/customer_data.csv")

# Sidebar menú
opcion = st.sidebar.selectbox(
    "Menú",
    ["Inicio", "Gráficos"]
)


# INICIO
# -------------------------
if opcion == "Inicio":
    st.subheader("Bienvenido 👋")
    st.write("Sistema de análisis de clientes con visualizaciones interactivas.")

    st.dataframe(df)
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
    "ID": int(cliente.id),
    "Edad": int(cliente.age),
    "Ingreso": int(cliente.income),
    "Frecuencia": cliente.purchase_frequency,
    "Monto compra": int(cliente.purchase_amount),
    "Satisfacción": int(cliente.satisfaction_score)
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

# -------------------------
# GRÁFICOS
# -------------------------
elif opcion == "Gráficos":

    st.header("📈 Visualizaciones")

    grafico = st.selectbox(
        "Seleccione un gráfico",
        [
            "Compra promedio por fidelización",
            "Distribución de clientes por región"
        ]
    )

    if grafico == "Compra promedio por fidelización":
        fig = grafico_compra_por_fidelizacion(df)
        st.pyplot(fig)

    elif grafico == "Distribución de clientes por región":
        fig = grafico_clientes_por_region(df)
        st.pyplot(fig)