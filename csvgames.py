import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Gráfico a partir de um arquivo CSV")

    # Carrega o arquivo CSV
    uploaded_file = st.file_uploader("Mobile_games.csv", type="csv")
    
    if uploaded_file is not None:
        # Lê o arquivo CSV
        df = pd.read_csv(uploaded_file)
        
        st.write("Exibindo os primeiros registros do arquivo:")
        st.write(df.head())

        # Seleciona as variáveis para o gráfico
        column1 = st.selectbox("Game Title", df.columns)
        column2 = st.selectbox("Player count", df.columns)

        # Plota o gráfico
        plt.figure(figsize=(10, 6))
        plt.scatter(df[column1], df[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f"Gráfico de dispersão entre {column1} e {column2}")
        st.pyplot()

if __name__ == "__main__":
    main()

