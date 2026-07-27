import streamlit as st

# ==========================================================
# LOAD CSS
# ==========================================================
def load_css():

    st.markdown("""
    <style>

    /* =====================================================
       IMPORT FONT
    ===================================================== */

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family: 'Poppins', sans-serif;
    }

    /* =====================================================
       COLOR PALETTE
    ===================================================== */

    :root{

        --primary:#D7B899;
        --secondary:#8B6B4A;
        --background:#F8F5F1;
        --white:#FFFFFF;
        --text:#2F2F2F;
        --border:#E5D6C7;
        --hover:#EFE2D4;

    }

    /* =====================================================
       BACKGROUND
    ===================================================== */

    .stApp{

        background-color:var(--background);

    }

    /* =====================================================
       HIDE DEFAULT STREAMLIT
    ===================================================== */

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    /* =====================================================
       HEADER
    ===================================================== */

    .header{

    background:linear-gradient(
        90deg,
        #D7B899,
        #E8D6C3
    );

    padding:28px;

    border-radius:20px;

    text-align:center;

    margin-bottom:35px;

    box-shadow:0 10px 25px rgba(0,0,0,.08);
}

    .header h1{

    margin:0;

    color:#3B2A1A;

    font-size:38px;

    font-weight:700;

    letter-spacing:2px;

}

    /* =====================================================
       SECTION TITLE
    ===================================================== */

    .section-title{

        font-size:28px;

        font-weight:700;

        color:#5E4631;

        margin-top:10px;

    }

    .section-subtitle{

        color:#777;

        font-size:16px;

        margin-bottom:20px;

    }

    /* =====================================================
       CARD
    ===================================================== */

    .card{

        background:white;

        border-radius:18px;

        padding:22px;

        border:1px solid var(--border);

        box-shadow:0px 4px 12px rgba(0,0,0,.06);

        margin-bottom:20px;

    }

    /* =====================================================
       DATASET CARD
    ===================================================== */
    .dataset-card{

        background:white;

        border-radius:20px;

        padding:25px;

        text-align:center;

        border:1px solid #E5D6C7;

        box-shadow:0 6px 15px rgba(0,0,0,.05);

        transition:all .3s ease;

        height:170px;

    }

.dataset-card:hover{

    transform:translateY(-6px);

    box-shadow:0 12px 24px rgba(0,0,0,.10);

}

.dataset-card h2{

    font-size:40px;

    color:#8B6B4A;

    margin-bottom:8px;

}

    /* =====================================================
       RESULT CARD
    ===================================================== */

    .result-card{

        background:white;

        border-left:7px solid #8B6B4A;

        border-radius:16px;

        padding:18px;

        box-shadow:0px 4px 12px rgba(0,0,0,.08);

        margin-bottom:10px;

    }

    .result-card h3{

        color:#8B6B4A;

        margin-bottom:8px;

    }

    .result-card h2{

        margin-top:0;

        font-size:28px;

        color:#2F2F2F;

    }

    /* =====================================================
       BUTTON
    ===================================================== */

    .stButton>button{

        width:100%;

        background:#8B6B4A;

        color:white;

        border:none;

        border-radius:10px;

        padding:12px;

        font-weight:600;

    }

    .stButton>button:hover{

        background:#6F5439;

        color:white;

    }

    /* =====================================================
       FILE UPLOADER
    ===================================================== */

    section[data-testid="stFileUploader"]{

        background:white;

        border-radius:15px;

        border:2px dashed #CDB79E;

        padding:15px;

    }

    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"]{

        background:#EFE2D4;

    }

    section[data-testid="stSidebar"] *{

        color:#3D2F21;

    }

    /* =====================================================
       TABLE
    ===================================================== */

    thead tr th{

        background:#D7B899 !important;

        color:black !important;

    }

    /* =====================================================
       METRIC
    ===================================================== */

    div[data-testid="metric-container"]{

        border-radius:15px;

        border:1px solid var(--border);

        background:white;

        padding:12px;

    }

    /* =====================================================
       IMAGE
    ===================================================== */

    img{

        border-radius:12px;

    }

    /* =====================================================
       PROGRESS BAR
    ===================================================== */

    .stProgress > div > div > div > div{

        background:#8B6B4A;

    }

    /* =====================================================
       FOOTER
    ===================================================== */

    .footer{

        background:#D7B899;

        margin-top:50px;

        padding:20px;

        border-radius:15px;

        text-align:center;

        color:black;

        line-height:1.8;

        box-shadow:0px -2px 10px rgba(0,0,0,.05);

    }

    /* =====================================================
       ANIMATION
    ===================================================== */

    .main{

        animation:fadeIn .5s ease;

    }

    @keyframes fadeIn{

        from{

            opacity:0;

            transform:translateY(8px);

        }

        to{

            opacity:1;

            transform:translateY(0);

        }

    }

/* ===============================
IMAGE GALLERY
=============================== */

.gallery-image img{

    border-radius:15px;

    border:2px solid #DDD;

    transition:.3s;

}

.gallery-image img:hover{

    transform:scale(1.03);

}

/* ===============================
UPLOAD BOX
=============================== */

section[data-testid="stFileUploader"]{

    border:3px dashed #B9936C;

    border-radius:18px;

    background:#FFFDFB;

}

/* ===============================
SIDEBAR
=============================== */

section[data-testid="stSidebar"]{

    border-right:2px solid #D8C2A8;

}
                
    </style>

    """, unsafe_allow_html=True)