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

with open("assets/class_names.json", "r") as f:
    class_names = json.load(f)

# ==========================================================
# LOAD MODEL
# ==========================================================

model_v2, model_v3 = load_models()


# ==========================================================
# PAGE
# ==========================================================

def classify_page():

    header()

    section_title(
        "Klasifikasi Citra",
        "Unggah citra motif batik untuk dilakukan proses klasifikasi menggunakan MobileNetV2 dan MobileNetV3."
    )

    st.markdown("### 📤 Upload Citra")

    uploaded_file = st.file_uploader(
        "Upload",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file is None:

        st.info("Silakan unggah citra batik terlebih dahulu.")

        footer()

        return

    image = Image.open(uploaded_file)

    st.divider()

    left, right = st.columns([1, 1.4])

    with left:

        st.markdown("### 🖼 Preview Citra")

        st.image(
            image,
            use_container_width=True
        )

    with st.spinner("Sedang melakukan klasifikasi..."):

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

    with right:

        st.markdown("### 🤖 Hasil Prediksi")

        c1, c2 = st.columns(2)

        with c1:

            prediction_card(
                "MobileNetV2",
                result_v2["label"],
                result_v2["confidence"],
                pred_v2,
                class_names
            )

        with c2:

            prediction_card(
                "MobileNetV3",
                result_v3["label"],
                result_v3["confidence"],
                pred_v3,
                class_names
            )

    st.divider()

    st.markdown("## 📊 Ringkasan Prediksi")

    summary = {
        "Model": [
            "MobileNetV2",
            "MobileNetV3"
        ],
        "Prediksi": [
            result_v2["label"],
            result_v3["label"]
        ],
        "Confidence (%)": [
            f"{result_v2['confidence']:.2f}",
            f"{result_v3['confidence']:.2f}"
        ]
    }

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    automatic_conclusion(
        result_v2["label"],
        result_v3["label"]
    )

    st.info(
        """
💡 **Tips Penggunaan**

- Gunakan citra motif batik yang jelas.
- Hindari gambar yang buram.
- Pastikan pencahayaan cukup.
- Format gambar yang didukung: JPG, JPEG, dan PNG.
"""
    )

    footer()
