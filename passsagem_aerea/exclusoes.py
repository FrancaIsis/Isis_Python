import sqlite3
from conexao import conectar


# função para excluir clientes
def excluir_cliente(cpf):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM clientes WHERE cpf = ?',(cpf,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cliente excluído com sucesso.')
    print('-'*70)


# função para excluir aeroportos
def excluir_aeroporto(aeroporto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM aeroportos WHERE aeroporto_id = ?',(aeroporto_id,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeroporto excluído com sucesso.')
    print('-'*70)

# função para excluir cidades
def excluir_cidade(cidade_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM cidades WHERE cidade_id = ?',(cidade_id,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cidade excluída com sucesso.')
    print('-'*70)

# função para excluir aeronaves
def excluir_aeronave(aeronave_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM aeronaves WHERE aeronave_id = ?',(aeronave_id,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeronave excluída com sucesso.')
    print('-'*70)


# função para excluir trecho
def excluir_trecho(trecho_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM trechos WHERE trecho_id = ?',(trecho_id,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho excluído com sucesso.')
    print('-'*70)

# função para excluir voo
def excluir_voo(voo_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM voos WHERE voo_id = ?',(voo_id,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Voo excluído com sucesso.')
    print('-'*70)
    
    
# função para excluir funcionario
def excluir_funcionario(cpf):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM funcionarios WHERE cpf = ?',(cpf,))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Funcionário excluído com sucesso.')
    print('-'*70)

