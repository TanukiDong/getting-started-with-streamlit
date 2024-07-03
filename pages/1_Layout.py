import streamlit as st

st.set_page_config(
    page_title="Layout",
    page_icon="1️⃣",
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Layout")

st.write("This is the first page about layout")

st.title("This is a Title")
st.caption("This is a caption")
st.write("This is a Text")
st.markdown("# This is a Markdown")
st.markdown("## This is a Markdown")
st.warning("This is a Warning")
st.error("This is an Error")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.success('This is a success message!', icon="✅")