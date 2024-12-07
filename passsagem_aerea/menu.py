import os
import sqlite3
from conexao import conectar
from insercoes import inserir_cliente
from insercoes import cadastrar_aeroporto
from insercoes import cadastrar_cidade
from insercoes import cadastrar_aeronave
from insercoes import cadastrar_trecho
from insercoes import cadastrar_voo
from insercoes import cadastrar_funcionario
from consultas import consultar_clientes, consultar_voos, consultar_aeroportos, consultar_cidades
from consultas import consultar_funcionarios, consultar_trechos, consultar_aeronaves

while True:

    usuario = int(input('Escolha uma opção: \n'
                        '1 - Sou cliente:\n'
                        '2 - Sou funcionário\n'
                        '3 - Sair\n'))

    if usuario == 1:
        while True:
            opcao = int(input('Informe a opção desejada:\n'
                              '1 - cadastrar clientes: \n'
                              '2 - cadastrar trecho:\n'
                              '3 - cadastrar voo: '
                              '10 - sair\n'))

            if opcao == 1:
                cpf = input('Informe o CPF do cliente: ')
                nome = input('Informe o nome do cliente: ')
                data_nascimento = input('Informe a data de nascimento: ')
                conectar()
                inserir_cliente(cpf, nome, data_nascimento)

            elif opcao == 2:
                distancia = input('Digite a distância: ')
                duracao = input('Digite o tempo de voo: ')
                aeroporto_origem = input('Digite o aeroporto de origem ')
                aeroporto_destino = input('Digite o aeroporto de destino ')
                conectar()
                cadastrar_trecho(distancia, duracao,
                                 aeroporto_origem, aeroporto_destino)

            elif opcao == 3:
                data = input('Informe a data desejada: ')
                horario = input('Digite o horário: ')
                aeronave_id = input('Digite o código da aeronave: ')
                trecho_id = input('Digite o código do trecho: ')
                conectar()
                cadastrar_voo(data, horario, aeronave_id, trecho_id)

    elif usuario == 2:

        while True:
            opcao = int(input('Informe a opção desejada:\n'
                              '1 - cadastrar clientes: \n'
                              '2 - cadastrar aeroportos:\n'
                              '3 - cadastrar cidades:\n'
                              '4 - cadastrar aeronaves:\n'
                              '5 - cadastrar trecho:\n'
                              '6 - cadastrar voo:\n'
                              '7 - cadastrar funcionario:\n'
                              '8 - visualizar clientes:\n'
                              '9 - visualizar voos:\n'
                              '10 - visualizar trechos:\n'
                              '11 - visualizar funcionarios:\n'
                              '12 - visualizar cidades:\n'
                              '13 - visualizar aeronaves:\n'
                              '14 - visualizar aeroportos:\n'
                              '100 - sair\n'))

            if opcao == 1:
                cpf = input('Informe o CPF do cliente: ')
                nome = input('Informe o nome do cliente: ')
                data_nascimento = input('Informe a data de nascimento: ')
                conectar()
                inserir_cliente(cpf, nome, data_nascimento)

            elif opcao == 2:
                nome_aeroporto = input('Digite o nome do aeroporto: ')
                cidade_id = input('Digite o codigo da cidade: ')
                conectar()
                cadastrar_aeroporto(nome_aeroporto, cidade_id)

            elif opcao == 3:
                nome_cidade = input('Digite o nome da cidade: ')
                estado = input('Digite o Estado: ')
                conectar()
                cadastrar_cidade(nome_cidade, estado)

            elif opcao == 4:
                nome_aeronave = input('Digite o nome/ tipo da aeronave: ')
                num_poltronas = input('Digite o numero de poltronas: ')
                conectar()
                cadastrar_aeronave(nome_aeronave, num_poltronas)

            elif opcao == 5:
                distancia = input('Digite a distância: ')
                duracao = input('Digite o tempo de voo: ')
                aeroporto_origem = input('Digite o aeroporto de origem ')
                aeroporto_destino = input('Digite o aeroporto de destino ')
                conectar()
                cadastrar_trecho(distancia, duracao,
                                 aeroporto_origem, aeroporto_destino)

            elif opcao == 6:
                data = input('Informe a data desejada: ')
                horario = input('Digite o horário: ')
                aeronave_id = input('Digite o código da aeronave: ')
                trecho_id = input('Digite o código do trecho: ')
                conectar()
                cadastrar_voo(data, horario, aeronave_id, trecho_id)

            elif opcao == 7:
                cpf = input('Informe o CPF do funcionario: ')
                nome_funcionario = input('Informe o nome do funcionario: ')
                conectar()
                cadastrar_funcionario(cpf, nome_funcionario)

            elif opcao == 8:
                conectar()
                consultar_clientes()

            elif opcao == 9:
                conectar()
                consultar_voos()

            elif opcao == 10:
                conectar()
                consultar_trechos()

            elif opcao == 11:
                conectar()
                consultar_funcionarios()

            elif opcao == 12:
                conectar()
                consultar_cidades()

            elif opcao == 13:
                conectar()
                consultar_aeronaves()

            elif opcao == 14:
                conectar()
                consultar_aeroportos()

            elif opcao == 100:
                print('Saindo...')
                break

            else:
                print('Opção inválida...')
                break

    elif usuario == 3:
        print('Saindo...')
        print()
        break

    else:
        print('Opção inválida.')
        print()
        break
