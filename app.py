import streamlit as st
import numpy as np
import joblib

# Cargar modelo entrenado
modelo = joblib.load("modelo_rf_optimizado.pkl")

# Diccionarios para mostrar opciones
combustible_dict = {"Diesel": 0, "Gasolina": 1}
transmision_dict = {"Manual": 0, "Automática": 1}

st.title("🚗 Predicción de Precio de Vehículos Usados")
st.write("Ingrese las características del vehículo para estimar su precio en dólares.")

# Entradas del usuario
año = st.number_input("📅 Año del vehículo", min_value=1990, max_value=2025, value=2018)
potencia = st.number_input("⚙️ Potencia máxima (bph)", min_value=30.0, max_value=300.0, value=90.0)
cilindrada = st.number_input("🔧 Cilindrada del motor (cc)", min_value=600, max_value=5000, value=1200)
km = st.number_input("🛣️ Kilometraje recorrido (km)", min_value=0, max_value=500000, value=60000)
combustible = st.selectbox("⛽ Tipo de combustible", list(combustible_dict.keys()))
transmision = st.selectbox("🔁 Tipo de transmisión", list(transmision_dict.keys()))

# Botón para predecir
if st.button("🔍 Estimar Precio"):
    entrada = np.array([[año, potencia, cilindrada, km, combustible_dict[combustible], transmision_dict[transmision]]])
    prediccion = modelo.predict(entrada)[0]

    st.success(f"💰 Precio estimado del vehículo: **${prediccion:,.2f}**")
