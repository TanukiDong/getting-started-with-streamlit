import streamlit as st
import time

st.set_page_config(
    page_title="Button",
    page_icon="4️⃣",
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Button")

st.write("This is the fourth page about button")

code = """ 
def hello()
    print("Hello, Streamlit!")
"""

if st.button("Hello"):
    st.markdown("Button has been clicked")
    st.code(code, language="python")

if st.button("Release the balloons"):
    with st.spinner('Inflating balloons...'):
        time.sleep(2)
    st.balloons()
    st.success('Balloons!')

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')