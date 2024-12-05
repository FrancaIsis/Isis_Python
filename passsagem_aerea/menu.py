import os
import sqlite3
from conexao import conectar
from insercoes import inserir_cliente

while True:
    opcao = input('Informe a opção desejada:\n1 - cadastrar clientes: \n2 - sair\n')
    
    if opcao == 1:
        cpf = input ('Informe o CPF do cliente: ')
        nome = input ('Informe o nome do cliente: ')
        data_nascimento = input('Informe a data de nascimento: ')
        conectar()
        inserir_cliente(cpf, nome, data_nascimento)
    if opcao == 2:
        print ('Saindo')
        break
        