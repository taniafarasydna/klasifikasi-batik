import os
from PIL import Image
import streamlit as st

from utils.components import (
    header,
    footer,
    section_title,
    dataset_summary,
    motif_table
)

# ==========================================================
# PATH
# ==========================================================

SAMPLE_PATH = "assets/sample_dataset"
PRIMARY_PATH = "assets/primer"


# ==========================================================
# DATA OVERVIEW PAGE
# ==========================================================

def overview_page():
    header()

    section_title(
        "Data Overview",
        "Informasi dataset yang digunakan dalam penelitian."
    )

    # ======================================================
    # DATASET SUMMARY
    # ======================================================

    total_count = 1370
    train_count = 1050
    test_count = 300
    primary_count = 20

    dataset_summary(
        total_count,
        15,
        train_count,
        test_count
    )

    st.write("")

    # ======================================================
    # DATASET INFORMATION
    # ======================================================

    st.markdown("## Dataset Penelitian")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>Dataset Sekunder</h4>
        <b>Sumber</b>
        Kaggle (2021)
        <b>Jumlah Citra</b>
        1.350 gambar
        <b>Jumlah Kelas</b>
        15 motif batik
        <b>Ukuran Citra</b>
        224 × 224 piksel
        </div>
        """, 
        unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <h4>Dataset Primer</h4>
        <b>Sumber</b>
        Dokumentasi Penelitian
        <b>Lokasi</b>
        Museum Batik TMII
        <b>Jumlah Citra</b>
        {primary_count} gambar
        <b>Tahun Pengambilan</b>
        2026
        </div>
        """, 
        unsafe_allow_html=True)

    # ======================================================
    # CONTOH DATASET SEKUNDER
    # ======================================================

    st.markdown("## Contoh Dataset Sekunder")
    st.write(
        "Berikut merupakan contoh citra dari masing-masing kelas motif batik "
        "yang digunakan sebagai dataset sekunder dalam penelitian."
    )

    if os.path.exists(SAMPLE_PATH):
        images = sorted([
            img for img in os.listdir(SAMPLE_PATH)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ])

        cols = st.columns(5)
        for i, img_name in enumerate(images):
            image = Image.open(
                os.path.join(SAMPLE_PATH, img_name)
            )
            with cols[i % 5]:
                st.image(
                    image,
                    use_container_width=True
                )
                st.caption(
                    os.path.splitext(img_name)[0]
                )
    else:
        st.warning("Folder sample_dataset tidak ditemukan.")

    # ======================================================
    # DATASET PRIMER
    # ======================================================

    st.markdown("## Dataset Primer")
    st.write(
        "Berikut merupakan citra primer yang diperoleh melalui pengambilan "
        "gambar secara langsung di Museum Batik TMII."
    )

    if os.path.exists(PRIMARY_PATH):
        images = sorted([
            img for img in os.listdir(PRIMARY_PATH)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ])

        cols = st.columns(4)
        for i, img_name in enumerate(images):
            img = Image.open(
                os.path.join(PRIMARY_PATH, img_name)
            )
            with cols[i % 4]:
                st.image(
                    img,
                    use_container_width=True
                )
                st.caption(f"Citra Primer {i+1}")
    else:
        st.warning("Folder primer tidak ditemukan.")

    # ======================================================
    # DAFTAR MOTIF BATIK
    # ======================================================

    st.markdown("## Daftar Motif Batik")
    motif_table()

    st.write("")
    footer()
