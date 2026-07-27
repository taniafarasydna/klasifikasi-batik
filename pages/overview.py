# ==========================================================
# IMPORT LIBRARY
# ==========================================================

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
# DATASET PATH
# ==========================================================

TRAIN_PATH = "data/DATASET/DATASET/TRAIN"
TEST_PATH = "data/DATASET/DATASET/TEST"
PRIMARY_PATH = "data/DATASET_PRIMER"


# ==========================================================
# COUNT IMAGE
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
# OVERVIEW PAGE
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

        st.markdown(
            """
            <div class="card">

            <h3>Dataset Sekunder</h3>

            <p><b>Sumber</b>
            Kaggle (2021)</p>

            <b>Jumlah Citra</b>
            1.350 gambar

            <p><b>Jumlah Kelas</b>
            15 motif batik Indonesia</p>

            <p><b>Ukuran Citra</b>
            224 × 224 piksel</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">

            <h3>Dataset Primer</h3>

            <p><b>Sumber</b><br>
            Dokumentasi Penelitian</p>

            <p><b>Lokasi</b><br>
            Museum Batik TMII</p>

            <p><b>Jumlah Citra</b><br>
            {primary_count} gambar</p>

            <p><b>Tahun Pengambilan</b><br>
            2026</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()
# ==========================================================
# DATASET SEKUNDER GALLERY
# ==========================================================

    st.markdown("## 🖼️ Contoh Dataset Sekunder")

    st.write(
        """
        Berikut merupakan contoh citra pada dataset sekunder 
        yang digunakan dalam proses pelatihan dan pengujian model.
        Setiap kelas direpresentasikan oleh satu contoh citra.
        """
    )


    if os.path.exists(TRAIN_PATH):

        class_folders = sorted([

            folder

            for folder in os.listdir(TRAIN_PATH)

            if os.path.isdir(
                os.path.join(
                    TRAIN_PATH,
                    folder
                )
            )

        ])


        cols = st.columns(5)


        for i, folder in enumerate(class_folders):

            folder_path = os.path.join(
                TRAIN_PATH,
                folder
            )


            images = sorted([

                img

                for img in os.listdir(folder_path)

                if img.lower().endswith(
                    (
                        ".jpg",
                        ".jpeg",
                        ".png"
                    )
                )

            ])


            if len(images) > 0:


                img_path = os.path.join(

                    folder_path,

                    images[0]

                )


                image = Image.open(
                    img_path
                )


                with cols[i % 5]:


                    st.image(

                        image,

                        use_container_width=True

                    )


                    st.caption(

                        folder

                    )


    else:

        st.warning(
            "Dataset sekunder tidak ditemukan."
        )



# ==========================================================
# DATASET PRIMER GALLERY
# ==========================================================

    st.markdown("## 📷 Dataset Primer")


    st.write(
        """
        Dataset primer merupakan citra batik yang diperoleh melalui
        dokumentasi langsung di Museum Batik TMII.
        Dataset ini digunakan sebagai data validasi untuk menguji
        kemampuan generalisasi model terhadap citra dunia nyata.
        """
    )


    if os.path.exists(PRIMARY_PATH):


        primary_images = sorted([

            img

            for img in os.listdir(PRIMARY_PATH)

            if img.lower().endswith(

                (
                    ".jpg",
                    ".jpeg",
                    ".png"
                )

            )

        ])



        if len(primary_images) > 0:


            cols = st.columns(5)


            for i, img_name in enumerate(primary_images):


                img_path = os.path.join(

                    PRIMARY_PATH,

                    img_name

                )


                image = Image.open(

                    img_path

                )


                with cols[i % 5]:


                    st.image(

                        image,

                        use_container_width=True

                    )


                    st.caption(

                        img_name

                    )



        else:

            st.info(
                "Dataset primer belum memiliki gambar."
            )


    else:

        st.warning(
            "Folder dataset primer tidak ditemukan."
        )



# ==========================================================
# MOTIF BATIK
# ==========================================================

    st.markdown(
        "## 📋 Daftar Kelas Motif Batik"
    )


    st.write(
        """
        Dataset yang digunakan terdiri atas 15 kelas motif batik
        Indonesia yang menjadi target klasifikasi model.
        """
    )


    motif_table()



# ==========================================================
# FOOTER
# ==========================================================

    footer()
    
