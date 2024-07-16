import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data",
    page_icon="3️⃣",
)

st.page_link("Home.py", label="Home", icon="🏠")

st.title("Data")

st.write("This is the third page about data")


df = pd.DataFrame({
    "First Column" : [1,2,3,4,5,6,7],
    "Second Column" : [11,33,55,77,66,44,22],
    "Third Column" : [100,90,80,70,60,50,40]
})

iris = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv")

# Data
st.header("Data")
st.dataframe(df.style.highlight_max(axis=0))

chart_btn = st.button("Show Chart")
if chart_btn:
    st.line_chart(df, x="First Column", y="Second Column")

st.write("Iris Data :")
st.dataframe(iris)
st.download_button(
    label="Download data as CSV",
    data=iris.to_csv().encode("utf-8"),
    file_name="iris.csv",
    mime="text/csv",
)

