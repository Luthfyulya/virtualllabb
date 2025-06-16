import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Turunan Pertama", layout="centered")

# Judul
st.title("🧮 Kalkulator Turunan Pertama")
st.markdown("Masukkan fungsi matematika dan lihat turunannya secara simbolik dan grafik.")

# Input fungsi
x = sp.symbols('x')
user_input = st.text_input("Masukkan fungsi f(x):", "x**2 + 3*x + 1")

try:
    # Parsing fungsi
    f = sp.sympify(user_input)

    # Turunan pertama
    f_prime = sp.diff(f, x)

    # Tampilkan hasil
    st.subheader("Hasil Turunan Pertama:")
    st.latex(f"f'(x) = {sp.latex(f_prime)}")

    # Plot fungsi dan turunannya
    st.subheader("Grafik Fungsi dan Turunan")
    f_lambdified = sp.lambdify(x, f, "numpy")
    f_prime_lambdified = sp.lambdify(x, f_prime, "numpy")

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)
    y_prime_vals = f_prime_lambdified(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="f(x)", color="blue")
    ax.plot(x_vals, y_prime_vals, label="f'(x)", color="red", linestyle="--")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
