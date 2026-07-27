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
# PATH DATASET
# ==========================================================

TRAIN_PATH = "data/DATASET/DATASET/TRAIN"
TEST_PATH = "data/DATASET/DATASET/TEST"
PRIMARY_PATH = "data/DATASET_PRIMER"


# ==========================================================
# COUNT IMAGES
# ==========================================================

def count_images(folder_path):

    total = 0

    if not os.path.exists(folder_path):
        return 0

    for root, _, files in os.walk(folder_path):

        total += len([
            f for f in files
            if f.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ])

    return total


# ==========================================================
# DATA OVERVIEW PAGE
# ==========================================================

def overview_page():

    header()

    section_title(
        "Data Overview",
        "Informasi dataset yang digunakan dalam penelitian."
    )

    train_count = count_images(TRAIN_PATH)

    test_count = count_images(TEST_PATH)

    primary_count = count_images(PRIMARY_PATH)

    total_count = train_count + test_count + primary_count

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

    st.markdown("## 📚 Dataset Penelitian")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h4>Dataset Sekunder</h4>

        <b>Sumber</b><br>
        Kaggle (2021)

        <br><br>

        <b>Jumlah Citra</b><br>
        1.350 gambar

        <br><br>

        <b>Jumlah Kelas</b><br>
        15 motif batik

        <br><br>

        <b>Ukuran</b><br>
        224 × 224 piksel

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="card">

        <h4>Dataset Primer</h4>

        <b>Sumber</b><br>
        Dokumentasi Penelitian

        <br><br>

        <b>Lokasi</b><br>
        Museum Batik TMII

        <br><br>

        <b>Jumlah Citra</b><br>
        {primary_count} gambar

        <br><br>

        <b>Tahun Pengambilan</b><br>
        2026

        </div>
        """, unsafe_allow_html=True)
    # ======================================================
    # CONTOH DATASET SEKUNDER
    # ======================================================

    st.markdown("## 🖼 Contoh Dataset Sekunder")

    if os.path.exists(TRAIN_PATH):

        class_folders = sorted([
            folder for folder in os.listdir(TRAIN_PATH)
            if os.path.isdir(os.path.join(TRAIN_PATH, folder))
        ])

        cols = st.columns(5)

        for i, folder in enumerate(class_folders):

            folder_path = os.path.join(TRAIN_PATH, folder)

            images = sorted([
                img for img in os.listdir(folder_path)
                if img.lower().endswith((".jpg", ".jpeg", ".png"))
            ])

            if images:

                image = Image.open(
                    os.path.join(folder_path, images[0])
                )

                with cols[i % 5]:

                    st.image(
                        image,
                        use_container_width=True
                    )

                    st.caption(folder)

    else:

        st.warning("Folder dataset sekunder tidak ditemukan.")
    # ======================================================
    # DATASET PRIMER
    # ======================================================

    st.markdown("## 📷 Dataset Primer")

    st.write(
        "Berikut merupakan citra primer yang diperoleh melalui "
        "pengambilan gambar secara langsung di Museum Batik TMII."
    )

    if os.path.exists(PRIMARY_PATH):

        images = sorted([

            img for img in os.listdir(PRIMARY_PATH)

            if img.lower().endswith(

                (".jpg", ".jpeg", ".png")

            )

        ])

        cols = st.columns(5)

        for i, img_name in enumerate(images):

            img = Image.open(

                os.path.join(

                    PRIMARY_PATH,

                    img_name

                )

            )

            with cols[i % 5]:

                st.image(

                    img,

                    use_container_width=True

                )

                st.caption(img_name)

    else:

        st.warning("Folder dataset primer tidak ditemukan.")
    # ======================================================
    # DATASET PRIMER
    # ======================================================

    st.markdown("## 📷 Dataset Primer")

    st.write(
        "Berikut merupakan citra primer yang diperoleh melalui "
        "pengambilan gambar secara langsung di Museum Batik TMII."
    )

    if os.path.exists(PRIMARY_PATH):

        images = sorted([

            img for img in os.listdir(PRIMARY_PATH)

            if img.lower().endswith(

                (".jpg", ".jpeg", ".png")

            )

        ])

        cols = st.columns(5)

        for i, img_name in enumerate(images):

            img = Image.open(

                os.path.join(

                    PRIMARY_PATH,

                    img_name

                )

            )

            with cols[i % 5]:

                st.image(

                    img,

                    use_container_width=True

                )

                st.caption(img_name)

    else:

        st.warning("Folder dataset primer tidak ditemukan.")
    # ======================================================
    # DAFTAR MOTIF BATIK
    # ======================================================

    st.markdown("## 📋 Daftar Motif Batik")

    motif_table()

    st.write("")

    footer()
