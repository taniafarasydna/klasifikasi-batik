# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
from streamlit_option_menu import option_menu

from utils.styles import load_css

from pages.overview import overview_page
from pages.classify import classify_page


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Klasifikasi Citra Motif Batik",
    page_icon="",
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
        <div style="text-align:center; padding:10px 0 20px 0;">
            <h2 style="margin-bottom:5px;color:#6F4E37;">
                Batik Classifier
            </h2>

            <p style="
                color:#777;
                font-size:14px;
                margin-top:0;
            ">
                Transfer Learning
                <br>
                MobileNetV2 & MobileNetV3
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(

        menu_title=None,

        options=[
            "Data Overview",
            "Klasifikasi"
        ],

        icons=[
            "database-fill",
            "camera-fill"
        ],

        default_index=0,

        styles={

            "container": {

                "padding": "8px",

                "background-color": "#EFE2D4",

                "border-radius": "15px"

            },

            "icon": {

                "color": "#8B6B4A",

                "font-size": "18px"

            },

            "nav-link": {

                "font-size": "16px",

                "text-align": "left",

                "margin": "6px",

                "--hover-color": "#D7B899",

                "border-radius": "10px",

            },

            "nav-link-selected": {

                "background-color": "#8B6B4A",

                "color": "white",

                "font-weight": "600",

            }

        }

    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center; font-size:13px; color:#666;">
            <b>Final Project</b><br>
            Informatika - Data Science
            <br><br>
            Universitas Bhayangkara Jakarta Raya
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# MAIN PAGE
# ==========================================================

if selected == "Data Overview":

    overview_page()

elif selected == "Klasifikasi":

    classify_page()
