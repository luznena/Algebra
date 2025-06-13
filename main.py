import streamlit as st
from fpdf import FPDF
import base64
from datetime import datetime

# Configuración inicial de la página
st.set_page_config(page_title="Examen Diagnóstico - Álgebra Lineal", layout="centered")

st.title("📝 Examen Diagnóstico – Álgebra Lineal")
st.markdown("Por favor responde las siguientes preguntas:")

# Preguntas del examen
preguntas = [
    {
        "texto": "¿Qué es el álgebra lineal?",
        "opciones": [
            "Un área de la geometría enfocada en figuras tridimensionales",
            "Una rama de las matemáticas que estudia vectores, matrices y sistemas lineales",
            "Un conjunto de fórmulas aplicadas en cálculo diferencial",
            "Un tema que solo se relaciona con la contabilidad"
        ]
    },
    {
        "texto": "¿Cuál de las siguientes opciones define mejor a un vector en álgebra lineal?",
        "opciones": [
            "Una función que mide la pendiente de una recta",
            "Una figura con forma de flecha que representa magnitud y dirección",
            "Una operación aritmética entre matrices",
            "Una constante sin unidades"
        ]
    },
    {
        "texto": "¿Qué indica obtener una fila como 0 = 5 al resolver un sistema de ecuaciones lineales?",
        "opciones": [
            "El sistema tiene infinitas soluciones",
            "El sistema tiene una única solución",
            "El sistema es inconsistente y no tiene solución",
            "El sistema tiene variables libres"
        ]
    },
    {
        "texto": "¿Qué significa obtener una fila completa de ceros en una matriz al resolver un sistema?",
        "opciones": [
            "Hay una solución única",
            "Hay un error de cálculo",
            "El sistema es inconsistente",
            "Hay variables libres e infinitas soluciones"
        ]
    },
    {
        "texto": "Un carpintero quiere construir una mesa de 12 metros de largo gastando exactamente $170 usando tablas tipo A ($30, 2 m) y tipo B ($40, 3 m). ¿Cuál es el sistema de ecuaciones que representa este problema?",
        "opciones": [
            "2x + 3y = 12,    30x + 40y = 170",
            "2x + 3y = 170,   30x + 40y = 12",
            "x + y = 12,      x + y = 170",
            "30x + 40y = 12,  2x + 3y = 170"
        ]
    },
    {
        "texto": "¿Cuál de los siguientes enunciados es falso respecto a una matriz?",
        "opciones": [
            "Una matriz puede representar un sistema de ecuaciones lineales",
            "Las filas de una matriz corresponden a ecuaciones",
            "Las columnas de una matriz representan variables",
            "Una matriz solo puede tener números positivos"
        ]
    },
    {
        "texto": "¿Qué propiedad permite intercambiar dos filas en una matriz sin alterar la solución del sistema?",
        "opciones": [
            "Conmutativa",
            "Distributiva",
            "Operación elemental",
            "Asociativa"
        ]
    },
    {
        "texto": "¿Cuál es la forma escalonada de una matriz?",
        "opciones": [
            "Cuando todas las entradas son cero",
            "Cuando la matriz tiene ceros debajo de la diagonal principal",
            "Cuando todos los números están ordenados alfabéticamente",
            "Cuando los vectores son ortogonales"
        ]
    },
    {
        "texto": "¿Qué representa geométricamente la solución de un sistema de ecuaciones lineales con dos incógnitas?",
        "opciones": [
            "Un punto, una recta o ninguna intersección",
            "Un triángulo",
            "Una parábola",
            "Un círculo"
        ]
    },
    {
        "texto": "Evalúa si la siguiente igualdad es verdadera o falsa: (2x+3)(x−1)−(x²+x−4) = 7−x",
        "opciones": [
            "Verdadera para todo valor de x",
            "Falsa para todo valor de x",
            "Verdadera solo si x = 1",
            "No se puede saber sin resolver"
        ]
    }
]

# Campos para nombre del estudiante
nombre = st.text_input("Nombre del alumno(a):")

# Respuestas del usuario
respuestas_usuario = []

# Generar preguntas dinámicamente
for i, p in enumerate(preguntas):
    st.markdown(f"### {i+1}. {p['texto']}")
    respuesta = st.radio("", options=p["opciones"], key=f"q{i}")
    respuestas_usuario.append(respuesta)

# Botón para guardar en PDF
if st.button("Guardar resultados en PDF") and nombre:
    
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Examen Diagnóstico – Álgebra Lineal", ln=True, align="C")
            self.ln(10)

        def add_answers(self, name, questions, answers):
            self.set_font("Arial", "", 12)
            self.cell(0, 10, f"Nombre: {name}", ln=True)
            self.cell(0, 10, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
            self.ln(10)
            for i, (q, a) in enumerate(zip(questions, answers)):
                self.multi_cell(0, 10, f"{i+1}. {q['texto']}")
                self.cell(0, 10, f"Respuesta: {a}", ln=True)
                self.ln(5)

    # Crear PDF
    pdf = PDF()
    pdf.add_page()
    pdf.add_answers(nombre, preguntas, respuestas_usuario)

    # Guardar en bytes
    pdf_output = pdf.output(dest='S').encode('latin-1')

    # Mostrar botón de descarga
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="examen_resultados.pdf">Descargar PDF</a>'
    st.success("✅ ¡Archivo PDF generado exitosamente!")
    st.markdown(href, unsafe_allow_html=True)

elif st.button("Guardar resultados en PDF") and not nombre:
    st.warning("⚠️ Por favor, ingresa el nombre del alumno antes de continuar.")
