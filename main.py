import streamlit as st
from fpdf import FPDF
import base64
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Examen Diagnóstico - Álgebra Lineal", layout="centered")

# Título
st.title("📝 Examen Diagnóstico – Álgebra Lineal")
st.markdown("Por favor responde las siguientes preguntas:")

# Nombre del alumno
nombre = st.text_input("Nombre del alumno(a):")

# Preguntas y opciones
preguntas = [
    {
        "texto": "1. ¿Qué es el álgebra lineal?",
        "opciones": [
            "Un área de la geometría enfocada en figuras tridimensionales",
            "Una rama de las matemáticas que estudia vectores, matrices y sistemas lineales",
            "Un conjunto de fórmulas aplicadas en cálculo diferencial",
            "Un tema que solo se relaciona con la contabilidad"
        ]
    },
    {
        "texto": "2. ¿Cuál de las siguientes opciones define mejor a un vector en álgebra lineal?",
        "opciones": [
            "Una función que mide la pendiente de una recta",
            "Una figura con forma de flecha que representa magnitud y dirección",
            "Una operación aritmética entre matrices",
            "Una constante sin unidades"
        ]
    },
    {
        "texto": "3. ¿Qué indica obtener una fila como 0 = 5 al resolver un sistema de ecuaciones lineales?",
        "opciones": [
            "El sistema tiene infinitas soluciones",
            "El sistema tiene una única solución",
            "El sistema es inconsistente y no tiene solución",
            "El sistema tiene variables libres"
        ]
    },
    {
        "texto": "4. ¿Qué significa obtener una fila completa de ceros en una matriz al resolver un sistema?",
        "opciones": [
            "Hay una solución única",
            "Hay un error de cálculo",
            "El sistema es inconsistente",
            "Hay variables libres e infinitas soluciones"
        ]
    },
    {
        "texto": "5. Un carpintero quiere construir una mesa de 12 metros de largo gastando exactamente 170 pesos usando tablas tipo A (30 pesos, 2 m) y tipo B (40 pesos, 3 m). ¿Cuál es el sistema de ecuaciones que representa este problema?",
        "opciones": [
            "2x + 3y = 12,    30x + 40y = 170",
            "2x + 3y = 170,   30x + 40y = 12",
            "x + y = 12,      x + y = 170",
            "30x + 40y = 12,  2x + 3y = 170"
        ]
    },
    {
        "texto": "6. ¿Cuál de los siguientes enunciados es falso respecto a una matriz?",
        "opciones": [
            "Una matriz puede representar un sistema de ecuaciones lineales",
            "Las filas de una matriz corresponden a ecuaciones",
            "Las columnas de una matriz representan variables",
            "Una matriz solo puede tener números positivos"
        ]
    },
    {
        "texto": "7. ¿Qué propiedad permite intercambiar dos filas en una matriz sin alterar la solución del sistema?",
        "opciones": [
            "Conmutativa",
            "Distributiva",
            "Operación elemental",
            "Asociativa"
        ]
    },
    {
        "texto": "8. ¿Cuál es la forma escalonada de una matriz?",
        "opciones": [
            "Cuando todas las entradas son cero",
            "Cuando la matriz tiene ceros debajo de la diagonal principal",
            "Cuando todos los números están ordenados alfabéticamente",
            "Cuando los vectores son ortogonales"
        ]
    },
    {
        "texto": "9. ¿Qué representa geométricamente la solución de un sistema de ecuaciones lineales con dos incógnitas?",
        "opciones": [
            "Un punto, una recta o ninguna intersección",
            "Un triángulo",
            "Una parábola",
            "Un círculo"
        ]
    },
    {
        "texto": "10. Evalúa si la siguiente igualdad es verdadera o falsa: (2x+3)(x−1)−(x²+x−4) = 7−x",
        "opciones": [
            "Verdadera para todo valor de x",
            "Falsa para todo valor de x",
            "Verdadera solo si x = 1",
            "No se puede saber sin resolver"
        ]
    }
]

# Guardar respuestas del usuario
respuestas_usuario = []

# Generar formulario dinámico
for i, p in enumerate(preguntas):
    st.markdown(f"### {p['texto']}")
    respuesta = st.radio("", options=p["opciones"], key=f"q{i}")
    respuestas_usuario.append(respuesta)

# Botón para generar PDF
if st.button("📥 Descargar resultados en PDF") and nombre:

    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "Examen Diagnóstico – Álgebra Lineal", ln=True, align="C")
            self.ln(5)
            self.set_font("Arial", "", 10)
            self.cell(0, 5, "Plantilla Interactiva con Resultados", ln=True, align="C")
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Página {self.page_no()}", align="C")

    # Crear PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Datos del encabezado
    pdf.cell(0, 10, f"Nombre: {nombre}", ln=True)
    pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(10)

    # Agregar preguntas y respuestas
    for i, (pregunta, respuesta) in enumerate(zip(preguntas, respuestas_usuario)):
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, pregunta["texto"])
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 8, f"Respuesta: {respuesta}")
        pdf.ln(8)

    # Salida del PDF en bytes
    pdf_output = pdf.output(dest='S').encode('latin-1')

    # Codificar para descarga
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="examen_resultados.pdf">📄 Haz clic aquí para descargar tu examen</a>'
    
    st.success("✅ ¡Archivo PDF generado exitosamente!")
    st.markdown(href, unsafe_allow_html=True)

elif st.button("📥 Descargar resultados en PDF") and not nombre:
    st.warning("⚠️ Por favor, ingresa el nombre del estudiante.")
