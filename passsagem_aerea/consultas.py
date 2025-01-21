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

def consultar_reservas(cpf_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas WHERE cpf_cliente = ?", (cpf_cliente,))
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
    
def consultar_reservas_geral():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas")
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
    
def consultar_detalhe_reserva(cpf_cliente):
    conn = conectar()
    cursor = conn.cursor()
    query = '''
            SELECT
                reservas.reserva_id,
                reservas.quantidade_passagens,
                reservas.cpf_cliente,
                ao.nome_aeroporto AS aeroporto_origem,
                ad.nome_aeroporto AS aeroporto_destino,
                trechos.preco AS preco,
                voos.horario AS horario
            FROM
                reservas
            INNER JOIN 
                voos ON reservas.voo_id = voos.voo_id
            INNER JOIN
                trechos ON voos.trecho_id = trechos.trecho_id
            INNER JOIN 
                aeroportos ao ON trechos.aeroporto_origem = ao.aeroporto_id
            INNER JOIN 
                aeroportos ad ON trechos.aeroporto_destino = ad.aeroporto_id
            WHERE 
                reservas.cpf_cliente = ?

                
            '''
    cursor.execute(query, (cpf_cliente,))
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
    
def consultar_detalhe_trechos(voo_id):
    conn = conectar()
    cursor = conn.cursor()
    query = '''
            SELECT 
                voos.voo_id,
                voos.data,
                voos.horario,
                ao.nome_aeroporto AS aeroporto_origem,
                ad.nome_aeroporto AS aeroporto_destino,
                trechos.trecho_id
            FROM 
                voos
            INNER JOIN 
                trechos ON voos.trecho_id = trechos.trecho_id
            INNER JOIN 
                aeroportos ao ON trechos.aeroporto_origem = ao.aeroporto_id
            INNER JOIN 
                aeroportos ad ON trechos.aeroporto_destino = ad.aeroporto_id
            WHERE 
                voos.voo_id = ?
            '''

    cursor.execute(query, (voo_id,))
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