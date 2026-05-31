import streamlit as st

def load_theme():

    st.markdown("""
    <style>

    .stApp{
        background:
        linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
        );

        color:white;
    }

    .main-title{

        font-size:4rem;

        font-weight:800;

        color:#00e5ff;

        text-shadow:
        0px 0px 20px
        rgba(0,229,255,.6);
    }

    .sub-title{

        font-size:1.2rem;

        color:#94a3b8;
    }

    div[data-testid="metric-container"]{

        background:
        rgba(15,23,42,.9);

        border:
        1px solid #00e5ff;

        border-radius:20px;

        padding:15px;

        box-shadow:
        0px 0px 15px
        rgba(0,229,255,.3);
    }

    h1,h2,h3{

        color:#00e5ff !important;
    }

    .glass{

        background:
        rgba(255,255,255,.05);

        backdrop-filter:
        blur(10px);

        border-radius:20px;

        padding:20px;
    }

    </style>
    """,
    unsafe_allow_html=True)