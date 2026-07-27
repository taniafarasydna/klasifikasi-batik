import json
import streamlit as st
from PIL import Image

from utils.styles import load_css

from utils.components import (
    header,
    footer,
    section_title,
    prediction_card,
    automatic_conclusion
)

from utils.model_loader import load_models

from utils.predictor import (
    predict_image,
    get_prediction_result
)

# ==========================================================
# LOAD CSS
# ==========================================================

load_css()

# ==========================================================
# LOAD CLASS NAME
# ==========================================================

with open("assets/class_names.json","r") as f:

    class_names = json.load(f)

# ==========================================================
# LOAD MODEL
# ==========================================================

model_v2, model_v3 = load_models()
# ==========================================================
# CLASSIFICATION PAGE
# ==========================================================

def classify_page():

    header()

    section_title(

        "Klasifikasi Citra",

        "Unggah citra batik untuk dilakukan proses klasifikasi."

    )

    uploaded_file = st.file_uploader(

        "Upload gambar",

        type=["jpg","jpeg","png"]

    )

    if uploaded_file is None:

        st.info(

            "Silakan upload citra batik terlebih dahulu."

        )

        footer()

        return
    image = Image.open(uploaded_file)

    st.markdown("### Preview Gambar")

    st.image(

        image,

        use_container_width=True

    )

    with st.spinner(

        "Sedang melakukan klasifikasi..."

    ):

        pred_v2, pred_v3 = predict_image(

            image,

            model_v2,

            model_v3

        )

    result_v2 = get_prediction_result(

        pred_v2,

        class_names

    )

    result_v3 = get_prediction_result(

        pred_v3,

        class_names

    )
    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        prediction_card(

            "MobileNetV2",

            result_v2["label"],

            result_v2["confidence"],

            pred_v2,

            class_names

        )

    with col2:

        prediction_card(

            "MobileNetV3",

            result_v3["label"],

            result_v3["confidence"],

            pred_v3,

            class_names

        )
    st.divider()

    st.markdown("## 📊 Ringkasan Prediksi")

    st.markdown(f"""

| Model | Hasil Prediksi | Confidence |
|------|-----------------|-----------|
| MobileNetV2 | **{result_v2["label"]}** | **{result_v2["confidence"]:.2f}%** |
| MobileNetV3 | **{result_v3["label"]}** | **{result_v3["confidence"]:.2f}%** |

""")

    automatic_conclusion(

        result_v2["label"],

        result_v3["label"]

    )

    footer()