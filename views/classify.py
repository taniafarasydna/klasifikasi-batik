import json
import streamlit as st
from PIL import Image

from utils.styles import load_css
from utils.components import (
    header,
    footer,
    section_title,
    prediction_card,
    automatic_conclusion,
    prediction_summary
)

from utils.model_loader import load_models
from utils.predictor import (
    predict_image,
    get_prediction_result
)

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
# CLASSIFICATION PAGE
# ==========================================================

def classify_page():
    header()
    section_title(
        "Klasifikasi Citra",
        "Unggah citra batik untuk dibandingkan menggunakan model MobileNetV2 dan MobileNetV3."
    )
    
    uploaded_file = st.file_uploader(
        "Unggah Gambar Batik",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        st.info(
            "Silakan unggah citra batik terlebih dahulu untuk memulai proses klasifikasi.")
        footer()
        return

    image = Image.open(uploaded_file)

    # ======================================================
    # PREVIEW
    # ======================================================

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Preview Citra")
        st.image(
            image,
            use_container_width=True
        )
        st.caption(
            f"**Nama File:** {uploaded_file.name}"
        )
        st.write(
            f"**Ukuran:** {image.size[0]} × {image.size[1]} piksel"
        )

    # ======================================================
    # PREDICTION
    # ======================================================

    with st.spinner("🔍 Sedang menganalisis motif batik..."):
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

    with col2:
        st.markdown("### Hasil Klasifikasi")
        left_card, right_card = st.columns(2)
        
        with left_card:
            prediction_card(
                "MobileNetV2",
                result_v2["label"],
                result_v2["confidence"],
                pred_v2,
                class_names
            )

        with right_card:
            prediction_card(
                "MobileNetV3",
                result_v3["label"],
                result_v3["confidence"],
                pred_v3,
                class_names
            )
    # ======================================================
    # RINGKASAN PREDIKSI
    # ======================================================

    st.divider()
    prediction_summary(
        result_v2,
        result_v3
    )

    # ======================================================
    # MODEL DENGAN CONFIDENCE TERTINGGI
    # ======================================================

    st.markdown("## 🏆 Model dengan Confidence Tertinggi")

    if result_v2["confidence"] > result_v3["confidence"]:
        st.success(
            f"""
**MobileNetV2** memberikan tingkat keyakinan tertinggi
dengan confidence **{result_v2['confidence']:.2f}%**.
"""
        )
    elif result_v3["confidence"] > result_v2["confidence"]:
        st.success(
            f"""
**MobileNetV3** memberikan tingkat keyakinan tertinggi
dengan confidence **{result_v3['confidence']:.2f}%**.
"""
        )
    else:
        st.info(
            f"""
Kedua model memiliki confidence yang sama,
yaitu **{result_v2['confidence']:.2f}%**.
"""
        )

    # ======================================================
    # KESIMPULAN
    # ======================================================

    automatic_conclusion(

        result_v2["label"],
        result_v3["label"]
    )

    # ======================================================
    # TIPS PENGGUNAAN
    # ======================================================

    st.markdown("## 💡 Tips Penggunaan")
    st.info(
        """
Agar hasil klasifikasi lebih optimal, perhatikan beberapa hal berikut:

- Gunakan gambar dengan pencahayaan yang baik.
- Pastikan motif batik terlihat jelas.
- Hindari gambar yang buram atau terpotong.
- Gunakan format JPG, JPEG, atau PNG.
- Sistem akan otomatis mengubah ukuran citra menjadi **224 × 224 piksel** sebelum proses klasifikasi.
"""
    )

    # ======================================================
    # FOOTER
    # ======================================================

    footer()
