# ==========================================================
# MODEL LOADER
# ==========================================================

import os
import streamlit as st
from tensorflow.keras.models import load_model


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_models():

    MODEL_V2 = "models/mobilenetv2_best.keras"
    MODEL_V3 = "models/mobilenetv3_best.keras"

    # -------------------------
    # Cek apakah model tersedia
    # -------------------------

    if not os.path.exists(MODEL_V2):
        st.error(f"Model tidak ditemukan:\n{MODEL_V2}")
        st.stop()

    if not os.path.exists(MODEL_V3):
        st.error(f"Model tidak ditemukan:\n{MODEL_V3}")
        st.stop()

    # -------------------------
    # Load model
    # -------------------------

    model_v2 = load_model(
        MODEL_V2,
        compile=False
    )

    model_v3 = load_model(
        MODEL_V3,
        compile=False
    )

    return model_v2, model_v3