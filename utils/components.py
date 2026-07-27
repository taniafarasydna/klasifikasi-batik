import streamlit as st
import pandas as pd
import numpy as np


# ==========================================================
# HEADER
# ==========================================================

def header():

    st.markdown("""
    <div class="header">

        <h1>🧵 KLASIFIKASI CITRA MOTIF BATIK</h1>

        <p>
            Sistem klasifikasi motif batik Indonesia menggunakan
            <b>Transfer Learning MobileNetV2 & MobileNetV3</b>
        </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown("""

    <div class="footer">

        <h4 style="margin-bottom:10px;">
            KLASIFIKASI CITRA BATIK INDONESIA
        </h4>

        Transfer Learning MobileNetV2 & MobileNetV3

        <br><br>

        Dibuat oleh

        <br>

        <b>Tania Fara Sayyidina</b>

        <br>

        202210715156

    </div>

    """, unsafe_allow_html=True)


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(title, subtitle=""):

    st.markdown(
        f"""
        <div class="section-title">
            {title}
        </div>

        <div class="section-subtitle">
            {subtitle}
        </div>
        """,
        unsafe_allow_html=True
    )
    # ==========================================================
# DATASET SUMMARY
# ==========================================================

def dataset_summary(total, classes, train, test):

    cards = [

        ("🖼️", total, "Total Citra"),

        ("🎨", classes, "Jumlah Motif"),

        ("📚", train, "Data Latih"),

        ("🧪", test, "Data Uji")

    ]

    cols = st.columns(4)

    for col, (icon, value, title) in zip(cols, cards):

        with col:

            st.markdown(f"""
            <div class="dataset-card">

                <div style="font-size:42px;">
                    {icon}
                </div>

                <h2>{value:,}</h2>

                <p>{title}</p>

            </div>
            """, unsafe_allow_html=True)
# ==========================================================
# CONFIDENCE BADGE
# ==========================================================

def confidence_badge(confidence):

    if confidence >= 95:

        st.success("🟢 Sangat Tinggi")

    elif confidence >= 80:

        st.info("🔵 Tinggi")

    elif confidence >= 60:

        st.warning("🟠 Sedang")

    else:

        st.error("🔴 Rendah")
# ==========================================================
# TOP 3 PREDICTION
# ==========================================================
# ==========================================================
# PREDICTION CARD
# ==========================================================

def prediction_card(
    model_name,
    label,
    confidence,
    prediction,
    class_names
):

    st.markdown(f"""
    <div class="result-card">

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">

            <h3 style="
            margin:0;
            color:#6F4E37;
            ">
            🤖 {model_name}
            </h3>

            <span style="
            background:#EFE2D4;
            padding:5px 12px;
            border-radius:15px;
            color:#6F4E37;
            font-size:12px;
            font-weight:600;
            ">
            AI Model
            </span>

        </div>

        <hr>

        <p style="
        text-align:center;
        color:#777;
        margin-bottom:5px;
        ">
        Hasil Prediksi
        </p>

        <h2 style="
        text-align:center;
        color:#3B2A1A;
        margin-top:0;
        margin-bottom:15px;
        ">
        {label}
        </h2>

    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence/100)

    confidence_badge(confidence)

    st.markdown("### 🏅 Top-3 Prediksi")
# ==========================================================
# PREDICTION CARD
# ==========================================================

def prediction_card(
    model_name,
    label,
    confidence,
    prediction,
    class_names
):

    st.markdown(f"""
    <div class="result-card">

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">

            <h3 style="
            margin:0;
            color:#6F4E37;
            ">
            🤖 {model_name}
            </h3>

            <span style="
            background:#EFE2D4;
            padding:5px 12px;
            border-radius:15px;
            color:#6F4E37;
            font-size:12px;
            font-weight:600;
            ">
            AI Model
            </span>

        </div>

        <hr>

        <p style="
        text-align:center;
        color:#777;
        margin-bottom:5px;
        ">
        Hasil Prediksi
        </p>

        <h2 style="
        text-align:center;
        color:#3B2A1A;
        margin-top:0;
        margin-bottom:15px;
        ">
        {label}
        </h2>

    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence/100)

    confidence_badge(confidence)

    st.markdown("### 🏅 Top-3 Prediksi")
    top3_prediction(
    prediction,
    class_names
)
# ==========================================================
# AUTOMATIC CONCLUSION
# ==========================================================

def automatic_conclusion(
    label_v2,
    label_v3
):

    st.markdown("---")

    st.markdown("## 📌 Kesimpulan Otomatis")

    if label_v2 == label_v3:

        st.success(f"""
### ✅ Kedua model menghasilkan prediksi yang sama

Motif batik yang diprediksi adalah:

## **{label_v2}**

Hal ini menunjukkan bahwa kedua model memiliki keputusan klasifikasi yang konsisten terhadap citra yang diuji.
""")

    else:

        st.warning("""
### ⚠️ Model memberikan prediksi yang berbeda.

Hasil klasifikasi MobileNetV2 dan MobileNetV3 tidak sama sehingga diperlukan analisis lebih lanjut terhadap citra yang diuji.
""")
# ==========================================================
# PREDICTION SUMMARY
# ==========================================================

def prediction_summary(
    result_v2,
    result_v3
):

    st.markdown("## 📊 Ringkasan Prediksi")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "MobileNetV2",

            result_v2["label"],

            f'{result_v2["confidence"]:.2f}%'

        )

    with col2:

        st.metric(

            "MobileNetV3",

            result_v3["label"],

            f'{result_v3["confidence"]:.2f}%'

        )
