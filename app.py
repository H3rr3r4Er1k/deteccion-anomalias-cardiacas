import streamlit as st
from utils import *

#Fronted hecho con la libreria streamlit

# Caracter铆sticas b谩sicas de la p谩gina
st.set_page_config(page_icon="馃搳", page_title="Detecci贸n de anomal铆as cardiacas", layout="wide")
st.image("https://miuceencasa.uce.edu.ec/wp-content/uploads/2020/07/logo_uce_modalidad_web.png", width=200)
st.title("Detecci贸n de anomal铆as cardiacas con autoencoders")

c29, c30, c31 = st.columns([1, 6, 1]) # 3 columnas: 10%, 60%, 10%

UMBRAL = 0.089

with c30:
    uploaded_file = st.file_uploader(
        "", type = 'pkl',
        key="1",
    )


    if uploaded_file is not None:
        file_container = st.expander("Verifique el archivo .pkl que acaba de subir")

        info_box_wait = st.info(
            f"""
                Realizando la clasificaci贸n...
                """)

        # Ac谩 viene la predicci贸n con el modelo
        dato = leer_dato(uploaded_file)
        autoencoder = Autoencoder()
        autoencoder = cargar_modelo_preentrenado('autoencoder.pth')
        prediccion = predecir(autoencoder, dato, UMBRAL)
        categoria = obtener_categoria(prediccion)


        # Y mostrar el resultado
        info_box_result = st.info(f"""
        	El dato analizado corresponde a un sujeto: {categoria}
        	""")

    else:
        st.info(
            f"""
                馃憜 Debe cargar primero un dato con extensi贸n .pkl
                """
        )

        st.stop()

