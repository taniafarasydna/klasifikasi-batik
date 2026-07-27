import streamlit as st
import pandas as pd
import numpy as np


# ==========================================================
# HEADER
# ==========================================================

def header():

    st.markdown(
        """
        <div class="header">

            <h1>🧵 KLASIFIKASI CITRA MOTIF BATIK</h1>

            <p>
            Sistem klasifikasi motif batik Indonesia menggunakan
            <b>Transfer Learning MobileNetV2 & MobileNetV3</b>
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown(
        """
        <div class="footer">

            <h4 style="margin-bottom:10px;">
                Klasifikasi Citra Motif Batik Indonesia
            </h4>

            <p style="margin:0;">
                Transfer Learning MobileNetV2 & MobileNetV3
            </p>

            <br>

            <p style="margin:0;">
                <b>Tania Fara Sayyidina</b><br>
                202210715156
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


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

    data = [

        ("🖼️", total, "Total Citra"),

        ("🎨", classes, "Jumlah Kelas"),

        ("📚", train, "Data Latih"),

        ("🧪", test, "Data Uji")

    ]

    cols = st.columns(4)

    for col, item in zip(cols, data):

        icon, value, title = item

        with col:

            st.markdown(
                f"""
                <div class="dataset-card">

                    <h1>{icon}</h1>

                    <h2>{value}</h2>

                    <p>{title}</p>

                </div>
                """,
                unsafe_allow_html=True
            )
# ==========================================================
# MOTIF TABLE
# ==========================================================

def motif_table():

    motif = [

        "Bali",
        "Betawi",
        "Cendrawasih",
        "Dayak",
        "Geblek Renteng",
        "Ikat Celup",
        "Insang",
        "Kawung",
        "Lasem",
        "Megamendung",
        "Pala",
        "Parang",
        "Poleng",
        "Sekar Jagad",
        "Tambal"

    ]

    df = pd.DataFrame({

        "No": np.arange(1, len(motif)+1),

        "Motif Batik": motif

    })

    st.dataframe(

        df,

        hide_index=True,

        use_container_width=True

    )


# ==========================================================
# CONFIDENCE BADGE
# ==========================================================

def confidence_badge(confidence):

    if confidence >= 95:

        st.success("🟢 Confidence Sangat Tinggi")

    elif confidence >= 80:

        st.info("🔵 Confidence Tinggi")

    elif confidence >= 60:

        st.warning("🟠 Confidence Sedang")

    else:

        st.error("🔴 Confidence Rendah")


# ==========================================================
# TOP 3 PREDICTION
# ==========================================================

def top3_prediction(prediction, class_names):

    top3_index = np.argsort(prediction)[::-1][:3]

    for rank, idx in enumerate(top3_index, start=1):

        confidence = prediction[idx] * 100

        st.write(
            f"**#{rank}. {class_names[idx]}**"
        )

        st.progress(confidence / 100)

        st.caption(
            f"{confidence:.2f}%"
        )


# ==========================================================
# PREDICTION SUMMARY
# ==========================================================

def prediction_summary(result_v2, result_v3):

    st.markdown("## 📊 Ringkasan Prediksi")

    df = pd.DataFrame({

        "Model":[

            "MobileNetV2",

            "MobileNetV3"

        ],

        "Hasil Prediksi":[

            result_v2["label"],

            result_v3["label"]

        ],

        "Confidence (%)":[

            f'{result_v2["confidence"]:.2f}%',

            f'{result_v3["confidence"]:.2f}%'

        ]

    })

    st.dataframe(

        df,

        hide_index=True,

        use_container_width=True

    )
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

    st.markdown(
        f"""
        <div class="result-card">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                margin-bottom:10px;
            ">

                <h3 style="
                    margin:0;
                    color:#6F4E37;
                ">
                    🤖 {model_name}
                </h3>

                <span style="
                    background:#EFE2D4;
                    padding:6px 12px;
                    border-radius:20px;
                    font-size:12px;
                    font-weight:600;
                    color:#6F4E37;
                ">
                    AI Model
                </span>

            </div>

            <hr>

            <p style="
                text-align:center;
                color:#888;
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
        """,
        unsafe_allow_html=True
    )

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(
        confidence / 100
    )

    confidence_badge(
        confidence
    )

    st.markdown("#### 🏅 Top-3 Prediksi")

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

    st.markdown("## 📌 Kesimpulan")

    if label_v2 == label_v3:

        st.success(
            f"""
### Kedua model memberikan hasil prediksi yang sama.

Motif batik yang diprediksi adalah:

## **{label_v2}**

Hal ini menunjukkan bahwa MobileNetV2 dan MobileNetV3 memiliki
kesepakatan terhadap hasil klasifikasi citra tersebut.
"""
        )

    else:

        st.warning(
            f"""
### Kedua model menghasilkan prediksi yang berbeda.

- **MobileNetV2** memprediksi: **{label_v2}**
- **MobileNetV3** memprediksi: **{label_v3}**

Perbedaan ini menunjukkan bahwa kedua model memiliki tingkat keyakinan
yang berbeda terhadap citra yang diuji.
"""
        )
