import streamlit as st
import pandas as pd
import numpy as np

# ==========================================================
# HEADER
# ==========================================================
def header():

    st.markdown("""
    <div class="header">

        <h1>KLASIFIKASI CITRA MOTIF BATIK</h1>

        <p style="
        margin-top:8px;
        color:#5F4630;
        font-size:18px;
        ">

        Sistem Klasifikasi Motif Batik Indonesia menggunakan
        <b>Transfer Learning MobileNetV2 & MobileNetV3</b>

        </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# FOOTER
# ==========================================================
def footer():

    st.markdown("""

    <br><br>

    <div class="footer">

    <b>Klasifikasi Citra Batik Indonesia</b>

    <br>

    Transfer Learning MobileNetV2 & MobileNetV3

    <br><br>

    dibuat oleh

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

    titles = [

        ("🖼", total, "Total Citra"),

        ("🎨", classes, "Jumlah Kelas"),

        ("📚", train, "Data Latih"),

        ("🧪", test, "Data Uji")

    ]

    cols = st.columns(4)

    for col, item in zip(cols, titles):

        icon, value, title = item

        with col:

            st.markdown(f"""

            <div class="dataset-card">

            <h1 style="font-size:42px">{icon}</h1>

            <h2>{value}</h2>

            <p>{title}</p>

            </div>

            """, unsafe_allow_html=True)

# ==========================================================
# DATASET SOURCE
# ==========================================================
def dataset_source():

    st.info("""

**Sumber Dataset**

Kaggle

Indonesian Batik Dataset

Dataset terdiri atas **15 kelas motif batik Indonesia**

Seluruh citra telah diseragamkan menjadi ukuran

**224 × 224 piksel**

sebelum dilakukan proses pelatihan model.

""")


# ==========================================================
# STRUCTURE DATASET
# ==========================================================
def dataset_structure():

    st.code("""

DATASET/

├── TRAIN/

│   ├── Bali

│   ├── Betawi

│   ├── Cendrawasih

│   ├── Dayak

│   ├── Geblek Renteng

│   ├── Ikat Celup

│   ├── Insang

│   ├── Kawung

│   ├── Lasem

│   ├── Megamendung

│   ├── Pala

│   ├── Parang

│   ├── Poleng

│   ├── Sekar Jagad

│   └── Tambal

│

└── TEST/

""")

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

        "No": np.arange(1, 16),

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
def confidence_badge(conf):

    if conf >= 95:

        st.success("🟢 Sangat Tinggi")

    elif conf >= 80:

        st.info("🟡 Tinggi")

    elif conf >= 60:

        st.warning("🟠 Sedang")

    else:

        st.error("🔴 Rendah")


# ==========================================================
# TOP 3 PREDICTION
# ==========================================================
def top3_prediction(pred, class_names):

    top = np.argsort(pred)[::-1][:3]

    data = []

    for idx in top:

        data.append({

            "Motif Batik": class_names[idx],

            "Confidence (%)": f"{pred[idx]*100:.2f}"

        })

    st.dataframe(

        pd.DataFrame(data),

        hide_index=True,

        use_container_width=True

    )


# ==========================================================
# RESULT CARD
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

    <h3 style="color:#8B6B4A;">
    🏆 {model_name}
    </h3>

    <hr>

    <h2 style="text-align:center;">
    {label}
    </h2>

    </div>

    """, unsafe_allow_html=True)

    st.progress(confidence/100)

    st.markdown(
        f"### Confidence : **{confidence:.2f}%**"
    )

    confidence_badge(confidence)

    st.markdown("#### Top-3 Prediction")

    top3_prediction(
        prediction,
        class_names
    )

# ==========================================================
# CONCLUSION
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
Kedua model memberikan hasil prediksi yang sama, yaitu
**{label_v2}**.
"""
        )

    else:

        st.warning(
            "Model memberikan prediksi yang berbeda."
        )

 