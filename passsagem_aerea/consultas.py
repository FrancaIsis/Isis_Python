import os
import sqlite3
from prettytable import PrettyTable
from conexao import conectar


# arquivo com funções de consultas ao banco de dados (clientes cadastrado, voo, reservas)

# função para consultar clientes
def consultar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()

# função para consultar voos
def consultar_voos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voos")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()
    
# função para consultar aeroportos
def consultar_aeroportos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aeroportos")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()
    
# função para consultar trechos
def consultar_trechos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trechos")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()
    
# função para consultar funcionarios
def consultar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()
    
# função para consultar cidades
def consultar_cidades():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cidades")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()
    
# função para consultar aeronaves
def consultar_aeronaves():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aeronaves")
    resultados = cursor.fetchall()

    os.system('cls')
    # criando a tabela
    tabela = PrettyTable()
    # obtendo os nomes das colunas
    colunas = [descricao[0] for descricao in cursor.description]
    # definindo o nome das colunas a partir da informaçao recebida da linha acima
    tabela.field_names = colunas

    # adicionando as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    print()
    print('*'*70)
    conn.close()