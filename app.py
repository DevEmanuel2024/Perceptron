import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================================
# CONFIGURACIÓN
# =========================================

st.set_page_config(
    page_title="Perceptrón Gamificado",
    layout="wide"
)

# =========================================
# ESTILOS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #050816;
    color: white;
}

.main-title {
    font-size: 50px;
    font-weight: bold;
    color: #00F5FF;
}

.subtitle {
    font-size: 20px;
    color: #BBBBBB;
    margin-bottom: 30px;
}

.card {
    background-color: #111827;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    border: 1px solid #1F2937;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #00F5FF;
}

.metric {
    font-size: 22px;
    font-weight: bold;
    color: #00FF88;
}

.small-text {
    color: #AAAAAA;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TÍTULO
# =========================================

st.markdown(
    '<div class="main-title">🧠 Perceptrón Gamificado</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ajusta manualmente los pesos y enseña a la neurona a clasificar patrones.</div>',
    unsafe_allow_html=True
)

# =========================================
# COLUMNAS
# =========================================

col1, col2 = st.columns([1, 2])

# =========================================
# PANEL IZQUIERDO
# =========================================

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎛️ Controles</div>',
        unsafe_allow_html=True
    )

    w1 = st.slider(
        "Peso w1",
        -10.0,
        10.0,
        1.0
    )

    w2 = st.slider(
        "Peso w2",
        -10.0,
        10.0,
        1.0
    )

    bias = st.slider(
        "Bias",
        -10.0,
        10.0,
        0.0
    )

    st.markdown("---")

    st.markdown(
        '<div class="metric">w1</div>',
        unsafe_allow_html=True
    )

    st.write("Importancia de x1")

    st.markdown(
        '<div class="metric">w2</div>',
        unsafe_allow_html=True
    )

    st.write("Importancia de x2")

    st.markdown(
        '<div class="metric">bias</div>',
        unsafe_allow_html=True
    )

    st.write("Qué tan fácil se activa la neurona")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎯 Salida Deseada</div>',
        unsafe_allow_html=True
    )

    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]

    targets = []

    for i, (x1, x2) in enumerate(inputs):

        objetivo = st.selectbox(
            f"({x1}, {x2})",
            [0, 1],
            key=i
        )

        targets.append(objetivo)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# RESULTADOS
# =========================================

resultados = []

correctos = 0

for i, (x1, x2) in enumerate(inputs):

    z = (w1 * x1) + (w2 * x2) + bias

    salida = 1 if z > 0 else 0

    correcto = salida == targets[i]

    if correcto:
        correctos += 1

    resultados.append({
        "x1": x1,
        "x2": x2,
        "z": round(z, 2),
        "Salida": salida,
        "Deseada": targets[i],
        "Correcto": correcto
    })

df = pd.DataFrame(resultados)

# =========================================
# PANEL DERECHO
# =========================================

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📈 Frontera de Decisión</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(8, 6))

    # Fondo
    ax.set_facecolor("#F8FAFC")

    # Puntos
    for i, (x1, x2) in enumerate(inputs):

        if targets[i] == 1:
            color = "lime"
        else:
            color = "red"

        ax.scatter(
            x1,
            x2,
            c=color,
            s=300,
            edgecolors="black"
        )

    # Línea
    x = np.linspace(-1, 2, 200)

    if w2 != 0:
        y = -(w1 * x + bias) / w2
        ax.plot(x, y, linewidth=3)

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📊 Resultados</div>',
        unsafe_allow_html=True
    )

    st.dataframe(df)

    st.markdown(
        f'<div class="metric">Patrones correctos: {correctos}/4</div>',
        unsafe_allow_html=True
    )

    if correctos == 4:
        st.success("✅ El perceptrón clasificó todo correctamente.")
    else:
        st.warning("⚠️ Sigue ajustando los pesos.")

    st.markdown('</div>', unsafe_allow_html=True)