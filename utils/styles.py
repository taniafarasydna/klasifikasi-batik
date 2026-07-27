import streamlit as st


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    st.markdown("""
<style>

/* ======================================================
   GOOGLE FONT
====================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html,
body,
[class*="css"]{

    font-family:'Poppins',sans-serif;

}


/* ======================================================
   COLOR PALETTE
====================================================== */

:root{

    --primary:#D7B899;
    --secondary:#8B6B4A;
    --background:#F8F5F1;
    --white:#FFFFFF;
    --text:#2F2F2F;
    --border:#E8D8C8;
    --hover:#EFE2D4;

}


/* ======================================================
   PAGE
====================================================== */

.stApp{

    background:var(--background);

}


/* ======================================================
   HIDE STREAMLIT DEFAULT
====================================================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}


/* ======================================================
   SIDEBAR
====================================================== */

section[data-testid="stSidebar"]{

    background:#EFE2D4;

    border-right:2px solid #DDC8B1;

}

section[data-testid="stSidebar"] *{

    color:#3B2A1A;

}


/* ======================================================
   HEADER
====================================================== */

.header{

    background:linear-gradient(
        135deg,
        #D7B899,
        #F2E6D8
    );

    border-radius:24px;

    padding:35px;

    text-align:center;

    margin-bottom:35px;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.header h1{

    margin:0;

    font-size:40px;

    font-weight:700;

    color:#3B2A1A;

}

.header p{

    margin-top:12px;

    color:#5E4631;

    font-size:18px;

}


/* ======================================================
   SECTION TITLE
====================================================== */

.section-title{

    font-size:30px;

    font-weight:700;

    color:#5E4631;

    margin-top:5px;

    margin-bottom:5px;

}

.section-subtitle{

    font-size:16px;

    color:#777;

    margin-bottom:25px;

}


/* ======================================================
   GENERAL CARD
====================================================== */

.card{

    background:white;

    border-radius:18px;

    padding:24px;

    border:1px solid var(--border);

    box-shadow:0 4px 14px rgba(0,0,0,.05);

}


/* ======================================================
   DATASET CARD
====================================================== */

.dataset-card{

    background:white;

    border-radius:18px;

    padding:24px;

    text-align:center;

    border:1px solid var(--border);

    transition:.25s;

    box-shadow:0 6px 15px rgba(0,0,0,.05);

}

.dataset-card:hover{

    transform:translateY(-6px);

    box-shadow:0 12px 25px rgba(0,0,0,.10);

}

.dataset-card h1{

    margin:0;

    font-size:40px;

}

.dataset-card h2{

    margin-top:10px;

    color:#8B6B4A;

}

.dataset-card p{

    color:#666;

}


/* ======================================================
   RESULT CARD
====================================================== */

.result-card{

    background:white;

    border-radius:18px;

    border-left:7px solid #8B6B4A;

    padding:20px;

    box-shadow:0 8px 20px rgba(0,0,0,.06);

    margin-bottom:18px;

}

.result-card:hover{

    transform:translateY(-3px);

    transition:.25s;

}

.result-card hr{

    border:none;

    border-top:1px solid #ECECEC;

    margin:15px 0;

}

.result-card h2{

    margin-top:0;

    color:#3B2A1A;

}

.result-card h3{

    margin:0;

    color:#6F4E37;

}


/* ======================================================
   METRIC
====================================================== */

div[data-testid="metric-container"]{

    border-radius:16px;

    background:white;

    border:1px solid var(--border);

    padding:12px;

    box-shadow:0 4px 10px rgba(0,0,0,.04);

}
/* ======================================================
   BUTTON
====================================================== */

.stButton > button{

    width:100%;

    background:#8B6B4A;

    color:white;

    border:none;

    border-radius:12px;

    padding:12px 20px;

    font-size:16px;

    font-weight:600;

    transition:0.3s;

}

.stButton > button:hover{

    background:#6F4E37;

    color:white;

    transform:translateY(-2px);

}


/* ======================================================
   FILE UPLOADER
====================================================== */

section[data-testid="stFileUploader"]{

    background:white;

    border:2px dashed #C8A988;

    border-radius:18px;

    padding:18px;

    box-shadow:0 4px 12px rgba(0,0,0,.04);

}


/* ======================================================
   IMAGE
====================================================== */

img{

    border-radius:15px;

}


/* ======================================================
   DATAFRAME
====================================================== */

thead tr th{

    background:#D7B899 !important;

    color:#3B2A1A !important;

    font-weight:600;

}

tbody tr:hover{

    background:#F7F2EC !important;

}


/* ======================================================
   PROGRESS BAR
====================================================== */

.stProgress > div > div > div > div{

    background:#8B6B4A;

}


/* ======================================================
   SUCCESS INFO WARNING
====================================================== */

div[data-testid="stAlert"]{

    border-radius:15px;

}


/* ======================================================
   DIVIDER
====================================================== */

hr{

    border:none;

    border-top:1px solid #E5D6C7;

}


/* ======================================================
   IMAGE GALLERY
====================================================== */

[data-testid="stImage"] img{

    border-radius:14px;

    transition:0.25s;

    border:2px solid #E8D8C8;

}

[data-testid="stImage"] img:hover{

    transform:scale(1.03);

}


/* ======================================================
   SCROLLBAR
====================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#C9A47A;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#F3EEE8;

}


/* ======================================================
   FOOTER
====================================================== */

.footer{

    margin-top:60px;

    background:#D7B899;

    border-radius:18px;

    padding:25px;

    text-align:center;

    color:#3B2A1A;

    line-height:1.8;

    box-shadow:0 5px 15px rgba(0,0,0,.05);

}


/* ======================================================
   ANIMATION
====================================================== */

.main{

    animation:fadeIn .45s ease;

}

@keyframes fadeIn{

    from{

        opacity:0;

        transform:translateY(12px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

</style>
""", unsafe_allow_html=True)
