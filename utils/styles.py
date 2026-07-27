import streamlit as st

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    st.markdown("""
<style>

/* =====================================================
GOOGLE FONT
===================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');


html,
body,
[class*="css"],
[data-testid="stAppViewContainer"]{

    font-family:'Poppins',sans-serif;

}


/* =====================================================
BACKGROUND
===================================================== */

.stApp{

    background:#F7F3EF;

}


/* =====================================================
REMOVE STREAMLIT DEFAULT
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
SCROLLBAR
===================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#EFE5DA;

}

::-webkit-scrollbar-thumb{

    background:#B68D5B;

    border-radius:20px;

}

::-webkit-scrollbar-thumb:hover{

    background:#8B6B4A;

}


/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{

    background:#EFE2D4;

    border-right:2px solid #DDC7AA;

}

section[data-testid="stSidebar"] *{

    color:#5B4634;

}

section[data-testid="stSidebar"] hr{

    border:1px solid #D4BEA5;

}


/* =====================================================
HEADER
===================================================== */

.header{

    background:linear-gradient(
    135deg,
    #D8B892,
    #F1E5D8
    );

    border-radius:25px;

    padding:35px;

    text-align:center;

    margin-bottom:35px;

    box-shadow:0 12px 30px rgba(0,0,0,.08);

}


.header h1{

    margin:0;

    font-size:42px;

    color:#49311F;

    font-weight:800;

    letter-spacing:2px;

}


.header p{

    margin-top:15px;

    color:#654C35;

    font-size:18px;

    line-height:1.7;

}


/* =====================================================
SECTION TITLE
===================================================== */

.section-title{

    font-size:30px;

    font-weight:700;

    color:#6B4B2E;

    margin-top:5px;

}


.section-subtitle{

    color:#7A7A7A;

    font-size:16px;

    margin-bottom:25px;

}


/* =====================================================
CARD
===================================================== */

.card{

    background:white;

    border-radius:18px;

    padding:22px;

    border:1px solid #E4D5C7;

    box-shadow:0 8px 20px rgba(0,0,0,.05);

    transition:.30s;

    margin-bottom:20px;

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 28px rgba(0,0,0,.09);

}


/* =====================================================
DATASET CARD
===================================================== */

.dataset-card{

    background:white;

    border-radius:20px;

    padding:30px;

    text-align:center;

    border:1px solid #E5D8CA;

    box-shadow:0 6px 20px rgba(0,0,0,.05);

    transition:.3s;

    height:180px;

}
.dataset-card:hover{

    transform:translateY(-8px);

    box-shadow:0 15px 30px rgba(0,0,0,.10);

}

.dataset-card h2{

    margin:10px 0 5px 0;

    font-size:40px;

    color:#8B6B4A;

    font-weight:700;

}

.dataset-card p{

    color:#666;

    font-size:15px;

}


/* =====================================================
RESULT CARD
===================================================== */

.result-card{

    background:#FFFFFF;

    border-radius:22px;

    padding:28px;

    border-left:8px solid #8B6B4A;

    box-shadow:0 8px 25px rgba(0,0,0,.08);

    transition:.30s;

    margin-bottom:20px;

}

.result-card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 35px rgba(0,0,0,.12);

}

.result-card h3{

    margin-top:0;

    color:#8B6B4A;

    text-align:center;

    font-size:24px;

    font-weight:700;

}

.result-card h2{

    margin-top:10px;

    text-align:center;

    color:#3D2D1F;

    font-size:32px;

    font-weight:700;

}


/* =====================================================
BUTTON
===================================================== */

.stButton>button{

    width:100%;

    background:#8B6B4A;

    color:white;

    border:none;

    border-radius:14px;

    padding:14px;

    font-weight:600;

    transition:.25s;

}

.stButton>button:hover{

    background:#6F4E37;

    transform:scale(1.02);

}


/* =====================================================
UPLOAD
===================================================== */

section[data-testid="stFileUploader"]{

    border:3px dashed #C49A6C;

    border-radius:20px;

    background:#FFFDFB;

    padding:18px;

}


/* =====================================================
IMAGE
===================================================== */

img{

    border-radius:16px;

}


/* =====================================================
DATAFRAME
===================================================== */

thead tr th{

    background:#D7B899 !important;

    color:#3D2D1F !important;

}

tbody tr:hover{

    background:#F6EFE7 !important;

}


/* =====================================================
PROGRESS BAR
===================================================== */

.stProgress > div > div > div > div{

    background:#8B6B4A;

}


/* =====================================================
METRIC
===================================================== */

div[data-testid="metric-container"]{

    border-radius:18px;

    border:1px solid #E6D8CA;

    background:white;

    padding:15px;

    box-shadow:0 5px 15px rgba(0,0,0,.05);

}


/* =====================================================
GALLERY
===================================================== */

.gallery-image{

    background:white;

    border-radius:18px;

    padding:12px;

    box-shadow:0 5px 18px rgba(0,0,0,.05);

    transition:.30s;

}

.gallery-image:hover{

    transform:translateY(-6px);

    box-shadow:0 10px 25px rgba(0,0,0,.10);

}

.gallery-image img{

    border-radius:14px;

}
/* =====================================================
SUCCESS - INFO - WARNING - ERROR
===================================================== */

div[data-testid="stAlert"]{

    border-radius:16px;

    border:none;

    box-shadow:0 5px 15px rgba(0,0,0,.05);

}


/* =====================================================
FOOTER
===================================================== */

.footer{

    margin-top:60px;

    background:linear-gradient(
        135deg,
        #D8B892,
        #EEDCC9
    );

    border-radius:22px;

    padding:28px;

    text-align:center;

    color:#3D2D1F;

    line-height:1.9;

    box-shadow:0 -5px 18px rgba(0,0,0,.06);

}

.footer b{

    color:#3D2D1F;

}


/* =====================================================
HORIZONTAL LINE
===================================================== */

hr{

    border:none;

    border-top:1px solid #E5D8CA;

    margin-top:15px;

    margin-bottom:15px;

}


/* =====================================================
PROGRESS TEXT
===================================================== */

.stMarkdown{

    color:#2F2F2F;

}


/* =====================================================
IMAGE CAPTION
===================================================== */

figcaption{

    text-align:center !important;

    font-weight:500;

    color:#6B4B2E !important;

    padding-top:8px;

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

        transform:translateY(15px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}


/* =====================================================
RESPONSIVE
===================================================== */

@media (max-width:900px){

    .header{

        padding:22px;

    }

    .header h1{

        font-size:30px;

        letter-spacing:1px;

    }

    .header p{

        font-size:15px;

    }

    .section-title{

        font-size:24px;

    }

    .dataset-card{

        height:auto;

        padding:20px;

    }

    .dataset-card h2{

        font-size:32px;

    }

    .result-card{

        padding:18px;

    }

    .result-card h2{

        font-size:26px;

    }

}


/* =====================================================
OPTION MENU
===================================================== */

.nav-link{

    border-radius:12px !important;

    transition:.25s;

}

.nav-link:hover{

    transform:translateX(4px);

}


/* =====================================================
REMOVE EXCESS PADDING
===================================================== */

.block-container{

    padding-top:2rem;

    padding-bottom:2rem;

}


/* =====================================================
END
===================================================== */

</style>
