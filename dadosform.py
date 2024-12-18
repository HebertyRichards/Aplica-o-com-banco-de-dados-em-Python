import sqlite3

# 1- Conectar no BD
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2- Inserir Dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute( 
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES (?, ?, ?)
    """, (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()
    
# 3 - Listagem de Dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados