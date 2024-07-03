import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.page_link("pages/1_Layout.py", label="Layout", icon="1️⃣")
st.page_link("pages/2_Input.py", label="Input", icon="2️⃣")
st.page_link("pages/3_Data.py", label="Data", icon="3️⃣")
st.page_link("pages/4_Button.py", label="Button", icon="4️⃣")

radio = st.radio(
    "Select Your Option",
    ("Apple", "Banana", "Carrot")
)
if radio:
    st.write(f"The option you choose is {radio}")

with st.sidebar:
    st.markdown("This is sidebar")
    st.page_link("http://www.google.com", label="Google", icon="🌎")
    st.page_link("http://www.youtube.com", label="Youtube", icon="🟥")

    sidebar_txt = st.text_input("Input your link")
    if sidebar_txt:
        f"[Click Me]({sidebar_txt})"

# Effect
st.header("Effect")
with st.echo():
    st.snow()
