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
        <div style="text-align:center;padding-top:10px;">

        <h2 style="
        color:#6F4E37;
        margin-bottom:5px;
        ">
        🧵 BATIK CLASSIFIER
        </h2>

        <p style="
        color:#8B6B4A;
        font-size:14px;
        ">
        Transfer Learning
        <br>
        MobileNetV2 & MobileNetV3
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

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

            "container":{

                "padding":"8px",

                "background-color":"#EFE2D4",

                "border-radius":"15px"

            },

            "icon":{

                "color":"#8B6B4A",

                "font-size":"20px"

            },

            "nav-link":{

                "font-size":"17px",

                "text-align":"left",

                "padding":"12px",

                "margin":"6px",

                "border-radius":"10px",

                "--hover-color":"#D7B899"

            },

            "nav-link-selected":{

                "background-color":"#8B6B4A",

                "color":"white"

            }

        }

    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center">

        <span style="font-size:13px;color:#6F4E37;">
        © 2026
        </span>

        <br>

        <b style="color:#6F4E37;">
        Tania Fara Sayyidina
        </b>

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================================
# ROUTING
# ==========================================================

if selected == "Data Overview":

    overview_page()

elif selected == "Klasifikasi":

    classify_page()
