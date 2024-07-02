import streamlit as st
import pandas as pd

with st.echo():
    st.title("Title")
    st.write("Write")
    st.markdown("## Markdown")

    code = """ 
    def hello()
        print("Hello, Streamlit!")
    """


    btn = st.button("Button")
    if btn:
        st.markdown("Button has been clicked")
        st.code(code, language="python")

    cols = st.columns(2)
    with cols[0]:
        num = st.number_input("Input number")
        st.markdown(f"Your number is {num}")

    with cols[1]:
        text = st.text_input("Input Text")
        text_tokenize = "|".join(text.split())
        st.markdown(f"{text_tokenize}")

    df = pd.DataFrame({
        "First Column" : [1,2,3,4],
        "Second Column" : [10,20,30,40]
    })
    st.dataframe(df)

    chart_btn = st.button("Show Chart")
    if chart_btn:
        st.line_chart(df, x="First Column", y="Second Column")