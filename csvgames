import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)


def show_chart(data):
    st.subheader("Gráfico a partir do arquivo CSV")
    st.line_chart(data)

def main():
    st.title("Exibindo um gráfico a partir de um arquivo CSV")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

    if uploaded_file is not None:
       
        data = load_data(uploaded_file)

       
        st.write("Dados do arquivo CSV:")
        st.write(data.head())

       
        show_chart(data)

if __name__ == "__main__":
    main()
