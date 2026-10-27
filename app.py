import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("کاوش تابع درجه دوم")
a = st.slider("ضریب a", -5.0, 5.0, 1.0, 0.1)
b = st.slider("ضریب b", -10.0, 10.0, 0.0, 0.5)
c = st.slider("ضریب c", -10.0, 10.0, 0.0, 0.5)

x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, linewidth=2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.set_title(f"y = {a}x² + {b}x + {c}")
ax.set_ylim(-30, 30)
st.pyplot(fig)
