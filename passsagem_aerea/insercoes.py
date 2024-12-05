import sqlite3
from conexao import conectar

def inserir_cliente(cpf, nome_cliente, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO clientes (cpf, nome_cliente, data_nascimento)
        VALUES (?,?,?)''',
        (cpf, nome_cliente, data_nascimento))  
    
    conn.commit()
    conn.close()
    

