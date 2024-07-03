import streamlit as st

st.set_page_config(
    page_title="Input",
    page_icon="2️⃣",
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Input")

st.write("This is the second page about input")

# Column
st.header("Column")
cols = st.columns(2)
with cols[0]:
    num = st.number_input("Input number", step=1)
    st.markdown(f"Your number is {num}")

with cols[1]:
    text = st.text_input("Input Text")
    text_tokenize = "|".join(text.split())
    st.markdown(f"Tokenized text is {text_tokenize}")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')