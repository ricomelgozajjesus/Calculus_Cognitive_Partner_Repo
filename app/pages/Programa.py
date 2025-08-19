# pages/01_Programa_Calculo_I.py
import os
import streamlit as st

# --- Safe resolver: env var -> secrets (guarded) -> default
def _resolve_base_url(default: str = "https://tu-dominio/calculo-i") -> str:
    env_val = os.environ.get("CALCULO_BASE_URL")
    if env_val:
        returngit init_env_val
    try:
        # This will raise if secrets.toml doesn't exist; we guard it.
        secrets_dict = dict(st.secrets)  # may raise
        return secrets_dict.get("CALCULO_BASE_URL", default)
    except Exception:
        return default

# Fallback for older Streamlit without st.link_button
def _link_button(label: str, url: str):
    try:
        st.link_button(label, url)
    except Exception:
        st.markdown(f"[{label}]({url})")

def render_programa_calculo_I(base_url: str = None):
    # ✅ use safe resolver (no direct st.secrets access here)
    base_url = base_url or _resolve_base_url()

    st.title("Compañero Cognitivo — Cálculo I")
    st.caption("Sílabus basado en el programa académico oficial (revisión Agosto 2008).")

    with st.expander("📘 Información general", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **Nombre:** Cálculo I")
            st.markdown("- **Clave:** CB0000-T")
            st.markdown("- **Horas por semana:** 5")
            st.markdown("- **Total de horas:** 80")
            st.markdown("- **Créditos:** 10")
        with col2:
            st.markdown("- **Prerrequisitos:** Ninguno")
            st.markdown("- **Antecedentes recomendados:** Álgebra, Trigonometría, Geometría Analítica")
            st.markdown("- **Objetivo general:**")
            st.markdown("  - Obtener la función derivada y antiderivada de funciones de una variable.")
            st.markdown("  - Interpretarlas geométricamente.")
            st.markdown("  - Aplicarlas a problemas prácticos.")

    with st.expander("🗂️ Programa sintético (distribución de horas)", expanded=True):
        st.markdown("""
- **1. Funciones y Límites – 20 h**
- **2. Primer Examen Parcial – 2 h**
- **3. La Derivada – 15 h**
- **4. Segundo Examen Parcial – 2 h**
- **5. Aplicaciones de la Derivada – 12 h**
- **6. Tercer Examen Parcial – 2 h**
- **7. La Integral – 25 h**
- **8. Cuarto Examen Parcial – 2 h**

**Total:** 80 h
        """)

    # ---- Contenido con ENLACES por unidad y subtema ----
    st.subheader("📖 Programa desarrollado (temario con enlaces)")
    programa = [
        {
            "id": "1", "titulo": "Funciones y Límites", "horas": 20, "slug": "funciones-limites",
            "subs": [
                ("1.1 Definición de función de una variable", "definicion-de-funcion"),
                ("1.2 Operaciones con funciones", "operaciones-con-funciones"),
                ("1.3 Definición de límite. Límites laterales", "limites-laterales"),
                ("1.4 Leyes para el cálculo de límites", "leyes-calculo-limites"),
                ("1.5 Técnicas especiales (racionales, irracionales racionalizables, exponenciales)", "tecnicas-especiales-limites"),
                ("1.6 Límites trigonométricos (p. ej. lim sin x / x)", "limites-trigonometricos"),
                ("1.7 Límites exponenciales (p. ej. (1+1/n)^n)", "limites-exponenciales"),
                ("1.8 Continuidad", "continuidad"),
                ("1.9 Sesión de uso de herramientas de cálculo simbólico", "herramientas-computacionales"),
            ],
        },
        {"id": "2", "titulo": "Primer Examen Parcial", "horas": 2, "slug": "examen-1",
         "subs": [("Guía y práctica", "guia")]},
        {
            "id": "3", "titulo": "La Derivada", "horas": 15, "slug": "la-derivada",
            "subs": [
                ("3.1 Definición e interpretación geométrica de la derivada", "definicion-interpretacion"),
                ("3.2 Reglas básicas (constante, suma, producto, cociente, cadena)", "reglas-basicas-derivacion"),
                ("3.3 Derivadas de funciones trascendentes", "derivadas-trascendentes"),
                ("3.4 Derivadas de orden superior", "derivadas-orden-superior"),
                ("3.7 Funciones implícitas y su derivación", "funciones-implicitas"),
                ("3.8 Diferenciales y fórmulas inmediatas", "diferencial-formulas"),
            ],
        },
        {"id": "4", "titulo": "Segundo Examen Parcial", "horas": 2, "slug": "examen-2",
         "subs": [("Guía y práctica", "guia")]},
        {
            "id": "5", "titulo": "Aplicaciones de la Derivada", "horas": 12, "slug": "aplicaciones-derivada",
            "subs": [
                ("5.1 Teoremas básicos (Rolle, Valor Medio)", "teoremas-basicos"),
                ("5.2 Regla de L’Hôpital", "regla-lhopital"),
                ("5.3 Máximos y mínimos", "maximos-minimos"),
                ("5.4 Criterio de la primera derivada", "primer-criterio-extremos"),
                ("5.5 Concavidad y criterio de la segunda derivada", "concavidad-segundo-criterio"),
                ("5.6 Ejemplos de optimización", "ejemplos-aplicacion"),
            ],
        },
        {"id": "6", "titulo": "Tercer Examen Parcial", "horas": 2, "slug": "examen-3",
         "subs": [("Guía y práctica", "guia")]},
        {
            "id": "7", "titulo": "La Integral", "horas": 25, "slug": "la-integral",
            "subs": [
                ("7.1 Integral indefinida", "integral-indefinida"),
                ("7.2 Reglas y sustitución simple", "reglas-sustitucion-simple"),
                ("7.3 Integral definida e interpretación geométrica", "integral-definida-interpretacion"),
                ("7.4 Teoremas fundamentales", "teoremas-integral-definida"),
                ("7.5 Aplicaciones (áreas, longitudes de arco, volúmenes/superficies de revolución)", "aplicaciones-integral"),
                ("7.6 Integración aproximada (rectángulos, trapecios, Simpson)", "integracion-aproximada"),
                ("7.7 Técnicas de integración (por partes, racionales, sustitución trigonométrica)", "tecnicas-integracion"),
            ],
        },
        {"id": "8", "titulo": "Cuarto Examen Parcial", "horas": 2, "slug": "examen-4",
         "subs": [("Guía y práctica", "guia")]},
    ]

    for unidad in programa:
        with st.container(border=True):
            st.markdown(f"### {unidad['id']}. {unidad['titulo']} ({unidad['horas']} h)")
            carpeta_unidad = f"{base_url}/{unidad['slug']}"
            _link_button("🔗 Abrir materiales de la unidad", carpeta_unidad)

            st.markdown(
                f"<div style='margin:.25rem 0 .5rem 0; color:#555'>"
                f"Sugerencia: <code>{unidad['slug']}/apuntes/</code>, "
                f"<code>{unidad['slug']}/ejercicios/</code>, <code>{unidad['slug']}/soluciones/</code>, "
                f"<code>{unidad['slug']}/videos/</code>, <code>{unidad['slug']}/datasets/</code>"
                f"</div>",
                unsafe_allow_html=True
            )
            for nombre, subslug in unidad["subs"]:
                st.markdown(f"- [{nombre}]({carpeta_unidad}/{subslug})")

    with st.expander("📚 Bibliografía", expanded=False):
        st.markdown("""
**Básica**  
- Larson, Hostetler, Edwards — *Cálculo I*, 8.ª ed., McGraw-Hill, ISBN 0-618-50298-X

**Complementaria**  
- Stewart — *Cálculo de una variable*, Vol. 1, 4.ª ed., Thomson Learning, ISBN 970-686-069-X  
- Ferreira Herrejón — *Notas de Cálculo Diferencial e Integral* (FIE)  
- Zill — *El Cálculo con Geometría Analítica* (Ed. Iberoamericana)  
- Edwards & Penny — *Cálculo con Geometría Analítica* (Prentice Hall)  
- Demidóvich — *Problemas y ejercicios de análisis matemático* (MIR)
        """)

    with st.expander("🧑‍🏫 Metodología y Evaluación", expanded=False):
        st.markdown("""
**Metodologías de enseñanza-aprendizaje**  
- Revisión de conceptos y resolución de problemas en clase  
- Lecturas fuera de clase  
- Tareas  
- Investigación documental  
- Uso de herramienta de cálculo simbólico

**Criterios de evaluación**  
- Asistencia  
- Tareas  
- Exámenes (departamentales/academia)
        """)
    st.caption("Revisión del programa: Agosto de 2008. Notas: conocimientos previos recomendados: Álgebra elemental, Trigonometría y Geometría Analítica.")

def main():
    render_programa_calculo_I()

if __name__ == "__main__":
    main()
