import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Funciones de una variable — Demo Interactiva")

func_type = st.selectbox(
    "Elige una función:",
    ["Lineal: f(x)=2x+1", "Cuadrática: f(x)=x^2", "Exponencial: f(x)=2^x"]
)

x = np.linspace(-2, 4, 200)

if func_type == "Lineal: f(x)=2x+1":
    y = 2*x + 1
elif func_type == "Cuadrática: f(x)=x^2":
    y = x**2
else:
    y = 2**x

fig, ax = plt.subplots()
ax.plot(x, y, label=func_type, linewidth=2)
ax.axhline(0, 0, 1)
ax.axvline(0, 0, 1)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
st.pyplot(fig)
