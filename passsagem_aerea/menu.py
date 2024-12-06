import os
import sqlite3
from conexao import conectar
from insercoes import inserir_cliente
from insercoes import cadastrar_aeroporto
from insercoes import cadastrar_cidade
from insercoes import cadastrar_aeronave

while True:
    opcao = int(input('Informe a opção desejada:\n'
                      '1 - cadastrar clientes: \n'
                      '2 - cadastrar aeroportos:\n'
                      '3 - cadastrar cidades:\n'
                      '4 - cadastrar aeronaves:\n'
                      '5 - cadastrar trecho:\n'
                      '10 - sair\n'))
    
    if opcao == 1:
        cpf = input ('Informe o CPF do cliente: ')
        nome = input ('Informe o nome do cliente: ')
        data_nascimento = input('Informe a data de nascimento: ')
        conectar()
        inserir_cliente(cpf, nome, data_nascimento)
        
    if opcao == 2:
        nome_aeroporto = input('Digite o nome do aeroporto: ')   
        cidade_id = input('Digite o codigo da cidade: ') 
        conectar()
        cadastrar_aeroporto(nome_aeroporto, cidade_id)
        
    if opcao == 3:
        nome_cidade = input('Digite o nome da cidade: ')   
        estado = input('Digite o Estado: ') 
        conectar()
        cadastrar_cidade(nome_cidade, estado)
        
    if opcao == 4:
        nome_aeronave = input('Digite o nome/ tipo da aeronave: ')   
        num_poltronas = input('Digite o numero de poltronas: ') 
        conectar()
        cadastrar_aeronave(nome_aeronave, num_poltronas)
    
    if opcao == 5:
        distancia = input('Digite a distância: ')   
        duracao = input('Digite o tempo de voo: ') 
        aeroporto_origem = input('Digite o aeroporto de origem ') 
        aeroporto_destino = input('Digite o aeroporto de destino ') 
        conectar()
        cadastrar_aeronave(distancia, duracao, aeroporto_origem, aeroporto_destino)
        
    if opcao == 10:
        print ('Saindo...')
        break
        