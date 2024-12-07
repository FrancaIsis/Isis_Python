import sqlite3

conn = sqlite3.connect("C:/Isis_Python/Isis_Python-1/passsagem_aerea/projetos_sqlite3/BD/aeroporto.db")

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

