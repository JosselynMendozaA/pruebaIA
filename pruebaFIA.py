import streamlit as st
import numpy as np

st.title("prueba IA ")
st.write("esta es una prueba")

# streamlit run pruebaFIA.py
# streamlit run "Actividad 13/ML_inference/IRIS/pruebaFIA.py"

frecuencia = st.slider("Select a frecuencia", 1, 10, 5)
x  = np.linspace(0, 10, 100)
y = np.sin(frecuencia * x)
st.line_chart(y)