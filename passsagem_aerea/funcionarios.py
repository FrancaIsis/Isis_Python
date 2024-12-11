import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        cpf TEXT NOT NULL PRIMARY KEY,
        nome_funcionario TEXT NOT NULL
        
    )
''')
