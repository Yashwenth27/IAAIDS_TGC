import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_navigation_bar import st_navbar
pages = ["Home", "About Us","Log out","","",""]


    
styles = {
    "nav": {
        "background-color": "green",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
st.set_page_config(initial_sidebar_state="collapsed",layout="wide",page_icon="🪴",page_title="Home Page")
page = st_navbar(pages, styles=styles, selected=None,logo_path="pages/Group 12.svg")
if page=="Home":
    if st.session_state["utype"]=="farmer":
        st.switch_page("pages/f_dash.py")
    elif st.session_state["utype"]=="customer":
        st.switch_page("pages/c_dash.py")
    elif st.session_state["utype"]=="wholer":
        st.switch_page("pages/w_dash.py")
if page=="About Us":
    st.switch_page("pages/About_Us.py")
if page=="Log out":
    st.switch_page("Home_Page.py")
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: green;
        color: white;
        width: 200px;
        text-alingn: center;
    }
    </style>""", unsafe_allow_html=True)
st.title("Soil Information")
# with c2: 
#     if st.button("Go Back"):
#         if st.session_state["utype"]=="farmer":
#             st.switch_page("pages/f_dash.py")
#         elif st.session_state["utype"]=="customer":
#             st.switch_page("pages/c_dash.py")
#         elif st.session_state["utype"]=="wholer":
#             st.switch_page("pages/w_dash.py")
#     if st.button("🔓Log Out"):
#         st.switch_page("pages/Logout.py")
st.markdown('<hr style="border: 4px solid green;">', unsafe_allow_html=True)

d,e = st.columns(2)
with d:
    with st.expander("Ideal N,P,K Values Info"):
        st.image("pages/npk_veg.png")
with e:
    with st.expander("Ideal pH Values Info"):
        st.image("pages/ph_veg.png")
a,b,c = st.columns(3)
with a:
    with st.container(border=True):
        st.metric(label="Nitrogen - N", value="20.1%", delta="-0.2%")
with b:
    with st.container(border=True):
        st.metric(label="Potassium - K", value="42.1%", delta="-3.2%")
with c:
    with st.container(border=True):
        st.metric(label="Phosphorous - P", value="12.4%", delta="5.6%")
z,x,c = st.columns(3)
with z:
    with st.container(border=True):
        st.metric(label="Humidity", value="31.3%", delta="1.2%")
with x:
    with st.container(border=True):
        st.metric(label="pH", value="7", delta="1.2")

rain(
    emoji="🌿",
    font_size=54,
    falling_speed=10,
    animation_length="infinite"
)

