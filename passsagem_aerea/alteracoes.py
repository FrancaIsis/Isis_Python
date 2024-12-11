import sqlite3
from conexao import conectar


# função para atualizar nome do cliente
def atualizar_nome_cliente(nome, cpf):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE clientes SET nome_cliente = ? WHERE cpf = ?',(cpf,nome))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cliente atualizado com sucesso.')
    print('-'*70)

# função para atualizar data de nascimento do cliente
def atualizar_data_nasc_cliente(data_nascimento, cpf):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE clientes SET data_nascimento = ? WHERE cpf = ?',(cpf,data_nascimento))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cliente atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar nome do aeroporto
def atualizar_nome_aeroporto(nome_aeroporto, aeroporto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE aeroportos SET nome_aeroporto = ? WHERE aeroporto_id = ?',(aeroporto_id, nome_aeroporto))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeroporto atualizado com sucesso.')
    print('-'*70)
    
def atualizar_cidade_aeroporto(cidade_id, aeroporto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE aeroportos SET cidade_id = ? WHERE aeroporto_id = ?',(aeroporto_id, cidade_id))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeroporto atualizado com sucesso.')
    print('-'*70)