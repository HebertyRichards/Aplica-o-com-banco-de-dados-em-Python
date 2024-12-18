import streamlit as st
import dadosform

st.title("Filmes")

nome = st.text_input("Nome do filme:")
ano = st.number_input("Ano do Filme:", min_value=1950, max_value=2024)
nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    dadosform.insere_dados(nome, ano, nota)
    st.success("Filme Cadastrado")
    
filmes = dadosform.obter_dados()
st.header("Lista de Filmes")
st.table(filmes)