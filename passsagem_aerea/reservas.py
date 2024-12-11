import sqlite3
from conexao import conectar

conn = conectar() 

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        reserva_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        quantidade_passagens INTEGER,
        cpf_cliente INTEGER,
        cpf_funcionario INTEGER,
        voo_id INTEGER,
        foreign key (cpf_cliente) references clientes (cpf_cliente),        
        foreign key (cpf_funcionario) references funcionarios (cpf_funcionario),
        foreign key (voo_id) references voos (voo_id)
    )
    
''')
conn.commit()
conn.close()

