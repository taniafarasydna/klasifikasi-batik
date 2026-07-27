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

def top3_prediction(prediction, class_names):

    top3 = np.argsort(prediction)[::-1][:3]

    st.markdown("#### 🏅 Top 3 Prediksi")

    for rank, idx in enumerate(top3, start=1):

        confidence = prediction[idx] * 100

        st.markdown(f"""
        <div class="card"
        style="
        margin-bottom:10px;
        padding:15px;
        ">

        <b>#{rank}</b>

        <br>

        {class_names[idx]}

        <br>

        <span style="
        color:#8B6B4A;
        font-weight:600;
        ">

        {confidence:.2f}%

        </span>

        </div>
        """, unsafe_allow_html=True)
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
            color:#8B6B4A;
            ">
            🏆 {model_name}
            </h3>

            <span style="
            background:#EFE2D4;
            padding:6px 14px;
            border-radius:20px;
            color:#6F4E37;
            font-size:13px;
            font-weight:600;
            ">
            AI Model
            </span>

        </div>

        <hr>

        <div style="text-align:center;">

            <div style="
            font-size:15px;
            color:#777;
            ">
            Hasil Prediksi
            </div>

            <div style="
            font-size:32px;
            font-weight:700;
            color:#3B2A1A;
            margin-top:10px;
            ">
            {label}
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)

    confidence_badge(confidence)

    st.write("")

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
