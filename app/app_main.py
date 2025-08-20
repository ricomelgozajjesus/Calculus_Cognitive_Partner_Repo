# app/app_main.py
import sys
from pathlib import Path
import yaml
import streamlit as st
from pages.Programa import render_programa_calculo_I

# --- Rutas robustas (funciona corriendo desde repo raíz o desde app/) ---
HERE = Path(__file__).resolve().parent          # .../repo/app
REPO_ROOT = HERE.parent                         # .../repo
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Import después de ajustar sys.path
from grader.rubric import grade_mcq  # requiere carpeta grader/ en la raíz del repo o dentro de app/

# --- Configuración de página ---
st.set_page_config(page_title="Cálculo I – Compañero Cognitivo", layout="wide")
st.title("🟢 Cálculo I – Compañero Cognitivo")
st.write("Práctica guiada, soluciones narradas y tu progreso en un solo lugar.")
# 1) Dónde podría estar tu HTML
CANDIDATE_PATHS = [
    Path("assets/funciones_1_1.html"),
    Path("static/funciones_1_1.html"),
    Path("funciones_1_1.html"),
]

def find_first_existing(paths):
    for p in paths:
        if p.exists():
            return p
    return None

def render_html_file(html_path: Path, *, height: int = 900, show_open_link: bool = True):
    """Lee un archivo HTML y lo incrusta dentro de la app."""
    try:
        html = html_path.read_text(encoding="utf-8")
    except Exception as e:
        st.error(f"No pude leer el archivo HTML en: {html_path}\n\nDetalle: {e}")
        return

    # Mostrar un enlace opcional para abrir en pestaña nueva
    if show_open_link:
        st.markdown(
            f'<div style="text-align:right">'
            f'<a href="{html_path.as_posix()}" target="_blank">🧩 Abrir en pestaña nueva</a>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # Incrustar el HTML en la página (como iframe)
    st.components.v1.html(html, height=height, scrolling=True)

# -------- Navegación sencilla en la barra lateral --------
st.sidebar.header("Unidad 1 · Funciones y modelos")
topic = st.sidebar.selectbox(
    "Selecciona un tema",
    ["Selecciona…", "1.1 Definición de función de una variable"]
)

st.title("Cálculo I · Funciones y modelos (una variable)")

if topic == "1.1 Definición de función de una variable":
    html_file = find_first_existing(CANDIDATE_PATHS)
    if html_file:
        st.subheader("1.1 Definición de función de una variable")
        render_html_file(html_file, height=900)
    else:
        st.error(
            "No encontré `funciones_1_1.html`. "
            "Colócalo en `assets/` o `static/` o en la raíz del proyecto, "
            "o edita `CANDIDATE_PATHS` para apuntar a tu ubicación real."
        )
        st.code("\n".join(str(p) for p in CANDIDATE_PATHS), language="bash")

# --- Sidebar / Navegación ---
page = st.sidebar.radio("Secciones", ["Diagnóstico", "Ejercicios", "Programa", "Progreso"])

# --- Utilidades ---
def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Banco de preguntas (ruta robusta)
bank_path = REPO_ROOT / "content" / "diagnostic_2025.yml"
bank = load_yaml(bank_path) if bank_path.exists() else []

# --- Sección: Diagnóstico ---
if page == "Diagnóstico":
    st.header("Diagnóstico")
    score = 0
    if not bank:
        st.warning("No se encontró el banco de diagnóstico en `content/diagnostic_2025.yml`.")
    else:
        for q in bank[:15]:
            st.subheader(q["stem"])
            idx = st.radio(
                "Elige una opción:",
                list(range(len(q["choices"]))),
                format_func=lambda i: q["choices"][i],
                key=q["id"]
            )
            if st.button(f"Calificar {q['id']}", key=f"btn-{q['id']}"):
                res = grade_mcq(q, idx)
                st.info("✔️ Correcto" if res["correct"] else "❌ Incorrecto")
                if res["correct"]:
                    score += 1
                with st.expander("Ver solución narrada"):
                    for step in q.get("solution_steps", []):
                        st.markdown(f"- {step}")
        st.success(f"Puntaje parcial (botones presionados): {score}/15")

# --- Sección: Ejercicios ---
elif page == "Ejercicios":
    st.header("Banco de ejercicios por tema")
    st.write("(Selecciona un tema en el sidebar en futuras iteraciones.)")

# --- NUEVA Sección: Programa (Syllabus) ---
elif page == "Programa":
    st.header("Programa de la Asignatura (Syllabus) – Cálculo I")

    # (Dentro de app_main.py, en la sección donde estaba tu sílabus original)

    st.subheader("Programa del curso (Sílabus)")
    st.markdown("Consulta el temario completo con enlaces para publicar materiales por tema y subtema.")

    # Enlace directo a la página multipágina de Streamlit
    try:
        # Streamlit 1.29+ tiene st.page_link
        st.page_link("pages/01_Programa_Calculo_I.py", label="📖 Abrir Programa – Cálculo I", icon="📘")
    except Exception:
        # Alternativa: un link normal si tu versión no soporta page_link
        st.link_button("📖 Abrir Programa – Cálculo I", url="#")  # Reemplaza con URL pública si lo sirves externo
# --- Sección: Progreso ---
else:
    st.header("Tu progreso")
    st.write("Resumen local (MVP). Próximamente: exportar CSV y perfil por estudiante.")