import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        cpf TEXT NOT NULL PRIMARY KEY,
        nome_cliente TEXT NOT NULL,
        data_nascimento TEXT NOT NULL
    )
''')