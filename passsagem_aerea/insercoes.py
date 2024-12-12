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
    print('-'*70)

# função para cadastrar aeroportos


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
    print('-'*70)


# função para cadastrar cidades
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
    print('-'*70)

# função para cadastrar aeronaves


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
    print('-'*70)

# função para cadastrar trechos


def cadastrar_trecho(distancia, duracao, preco, aeroporto_origem, aeroporto_destino):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO trechos (distancia, duracao, preco, aeroporto_origem, aeroporto_destino)
        VALUES (?,?,?,?)''',
                   (distancia, duracao, preco, aeroporto_origem, aeroporto_destino))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho cadastrado com sucesso.')
    print('-'*70)


# função para cadastrar voos
def cadastrar_voo(data, horario, aeronave_id, trecho_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO voos (data, horario, aeronave_id, trecho_id)
        VALUES (?,?,?,?)''',
                   (data, horario, aeronave_id, trecho_id))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Voo cadastrado com sucesso.')
    print('-'*70)

    

# função para cadastrar funcionarios
def cadastrar_funcionario(cpf, nome_funcionario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO funcionarios (cpf, nome_funcionario)
        VALUES (?,?)''',
                   (cpf, nome_funcionario))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Funcionario cadastrado com sucesso.')
    print('-'*70)
