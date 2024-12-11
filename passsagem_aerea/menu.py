import os
import sqlite3
from conexao import conectar
from insercoes import inserir_cliente, cadastrar_aeroporto, cadastrar_cidade,cadastrar_aeronave, cadastrar_trecho
from insercoes import cadastrar_voo
from insercoes import cadastrar_funcionario
from consultas import consultar_clientes, consultar_voos, consultar_aeroportos, consultar_cidades
from consultas import consultar_funcionarios, consultar_trechos, consultar_aeronaves
from exclusoes import excluir_cliente, excluir_aeroporto
from exclusoes import excluir_cidade, excluir_aeronave, excluir_trecho, excluir_voo, excluir_funcionario, excluir_aeronave
from alteracoes import atualizar_data_nasc_cliente, atualizar_nome_cliente, atualizar_cidade_aeroporto, atualizar_nome_aeroporto


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
                              '15 - excluir clientes:\n'
                              '16 - excluir aeroportos:\n'
                              '17 - excluir cidade:\n'
                              '18 - excluir aeronave:\n'
                              '19 - excluir trecho:\n'
                              '20 - excluir voo:\n'
                              '21 - excluir funcionário:\n'
                              '22 - alterar cliente:\n'
                              '23 - alterar aeroporto:\n'
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
                
                consultar_clientes()

            elif opcao == 9:
                
                consultar_voos()

            elif opcao == 10:
                
                consultar_trechos()

            elif opcao == 11:
                
                consultar_funcionarios()

            elif opcao == 12:
                
                consultar_cidades()

            elif opcao == 13:
                
                consultar_aeronaves()

            elif opcao == 14:
                
                consultar_aeroportos()
                
            elif opcao == 15:
                
                consultar_clientes()
                cpf = input('Digite o CPF do cliente a ser excluído: ')
                excluir_cliente(cpf)
                
            elif opcao == 16:
                
                consultar_aeroportos()
                aeroporto_id = int(input('Digite o código do aeroporto a ser excluído: '))
                excluir_aeroporto(aeroporto_id)
                
            elif opcao == 17:
                
                consultar_cidades()
                cidade_id = int(input('Digite o código da cidade a ser excluída: '))
                excluir_cidade(cidade_id)

            elif opcao == 18:
                
                consultar_trechos()
                trecho_id = int(input('Digite o código do trecho a ser excluído: '))
                excluir_trecho(trecho_id)
                
            elif opcao == 19:
                
                consultar_aeronaves()
                aeronave_id = int(input('Digite o código da aeronave a ser excluída: '))
                excluir_aeronave(aeronave_id)
                
            elif opcao == 20:
                
                consultar_voos()
                voo_id = int(input('Digite o código do voo a ser excluído: '))
                excluir_voo(voo_id)
                
            elif opcao == 21:
                
                consultar_funcionarios()
                cpf = input('Digite o cpf do funcionário a ser excluído: ')
                excluir_funcionario(cpf)
                
            elif opcao == 22:
                
                consultar_clientes()
                cpf = input('Digite o cpf do cliente a ser atualizado: ')
                atualiza = int(input('O que deseja alterar?\n'
                                     '1 - nome\n'
                                     '2 - data de nascimento\n'))
                if atualiza == 1:
                    nome = input('Digite o novo nome do cliente: \n')
                    atualizar_nome_cliente(cpf, nome)
                elif atualiza ==2:
                    data_nascimento = input('Digite a data de nascimento correta: \n')
                    atualizar_data_nasc_cliente(cpf, data_nascimento)
                    
            elif opcao == 23:
                
                consultar_aeroportos()
                aeroporto_id = int(input('Digite o código do aeroporto a ser atualizado: '))
                atualiza = int(input('O que deseja alterar?\n'
                                     '1 - nome\n'
                                     '2 - cidade\n'))
                if atualiza == 1:
                    nome = input('Digite o novo nome do aeroporto: \n')
                    atualizar_nome_aeroporto(aeroporto_id, nome)
                elif atualiza ==2:
                    cidade_id = int(input('Digite o código da cidade correta: \n'))
                    atualizar_cidade_aeroporto(aeroporto_id,cidade_id)

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
