import sqlite3
from conexao import conectar


# função para cadastrar clientes
def inserir_cliente(cpf, nome_cliente, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO clientes (cpf, nome_cliente, data_nascimento)
        VALUES (?,?,?)''',
                   (cpf, nome_cliente, data_nascimento))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cliente cadastrado com sucesso.')


#função para cadastrar aeroportos
def cadastrar_aeroporto(nome_aeroporto, cidade_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO aeroportos (nome_aeroporto, cidade_id)
        VALUES (?,?)''',
                   (nome_aeroporto, cidade_id))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeroporto cadastrado com sucesso.')
    

#função para cadastrar cidades
def cadastrar_cidade(nome_cidade, estado):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cidades (nome_cidade, estado)
        VALUES (?,?)''',
                   (nome_cidade, estado))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cidade cadastrada com sucesso.')
    
#função para cadastrar aeronaves
def cadastrar_aeronave(nome_aeronave, num_poltronas):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO aeronaves (nome_aeronave, num_poltronas)
        VALUES (?,?)''',
                   (nome_aeronave, num_poltronas))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeronave cadastrada com sucesso.')
    
#função para cadastrar trechos
def cadastrar_trecho(distancia, duracao, aeroporto_origem, aeroporto_destino):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO trechos (distancia, duracao, aeroporto_origem, aeroporto_destino)
        VALUES (?,?,?,?)''',
                   (distancia, duracao, aeroporto_origem, aeroporto_destino))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho cadastrada com sucesso.')