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
 
# função para atualizar cidade do aeroporto  
def atualizar_cidade_aeroporto(cidade_id, aeroporto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE aeroportos SET cidade_id = ? WHERE aeroporto_id = ?',(aeroporto_id, cidade_id))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeroporto atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar nome da cidade
def atualizar_nome_cidade(nome_cidade, cidade_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE cidades SET nome_cidade = ? WHERE cidade_id = ?',(cidade_id, nome_cidade))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cidade atualizada com sucesso.')
    print('-'*70)
    
# função para atualizar o estado da cidade
def atualizar_estado_cidade(estado, cidade_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE cidades SET estado = ? WHERE cidade_id = ?',(cidade_id, estado))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Cidade atualizada com sucesso.')
    print('-'*70)
    
# função para atualizar o nome/tipo da aeronave
def atualizar_nome_aeronave(nome_aeronave, aeronave_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE aeronaves SET nome_aeronave = ? WHERE aeronave_id = ?',(aeronave_id, nome_aeronave))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeronave atualizada com sucesso.')
    print('-'*70)
    
# função para atualizar o numero de poltronas da aeronave
def atualizar_poltrona_aeronave(num_poltronas, aeronave_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE aeronaves SET num_poltronas = ? WHERE aeronave_id = ?',(aeronave_id, num_poltronas))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Aeronave atualizada com sucesso.')
    print('-'*70)
    
    
# função para atualizar a distancia e o tempo de duração de um trecho
def atualizar_distancia_duracao_trecho(distancia, duracao, trecho_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE trechos SET distancia = ? duracao = ? WHERE trecho_id = ?',(trecho_id, distancia, duracao))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar a origem e destino de um trecho
def atualizar_origem_destino_trecho(aeroporto_origem, aeroporto_destino, trecho_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE trechos SET aeroporto_origem = ? aeroporto_destino = ? WHERE trecho_id = ?',(trecho_id, aeroporto_origem, aeroporto_destino))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar o preço de um trecho
def atualizar_preco_trecho(preco, trecho_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE trechos SET preco = ? WHERE trecho_id = ?',(trecho_id, preco))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Trecho atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar data e horario de um voo
def atualizar_data_horario_voo(data, horario, voo_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE voos SET data = ? horario = ? WHERE voo_id = ?',(voo_id, data, horario))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Voo atualizado com sucesso.')
    print('-'*70)
    
# função para atualizar aeeronave e trecho de um voo
def atualizar_aeronave_trecho_voo(aeronave_id, trecho_id, voo_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE voos SET aeronave_id = ? trecho_id = ? WHERE voo_id = ?',(voo_id, aeronave_id, trecho_id))

    conn.commit()
    conn.close()
    print('-'*70)
    print('Voo atualizado com sucesso.')
    print('-'*70)