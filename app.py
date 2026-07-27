import streamlit as st
from streamlit_option_menu import option_menu

from utils.styles import load_css

from pages.overview import overview_page
from pages.classify import classify_page


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Klasifikasi Citra Motif Batik",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# LOAD CSS
# ==========================================================

load_css()


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown(
        """
        <h2 style="text-align:center;color:#8B6B4A;">
        🧵 Batik Classifier
        </h2>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(

        menu_title="",

        options=[
            "Data Overview",
            "Klasifikasi"
        ],

        icons=[
            "database",
            "camera"
        ],

        menu_icon="cast",

        default_index=0,

        styles={

            "container": {
                "padding": "5px",
                "background-color": "#EFE2D4"
            },

            "icon": {
                "color": "#8B6B4A",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#D7B899",
            },

            "nav-link-selected": {
                "background-color": "#8B6B4A",
            },

        }
    )

    st.markdown("---")

    st.caption(
        "Transfer Learning\n\n"
        "MobileNetV2 & MobileNetV3"
    )


# ==========================================================
# ROUTING
# ==========================================================

if selected == "Data Overview":

    overview_page()

elif selected == "Klasifikasi":

    classify_page()