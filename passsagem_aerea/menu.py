import os
import sqlite3
from conexao import conectar
from insercoes import inserir_cliente, cadastrar_aeroporto, cadastrar_cidade,cadastrar_aeronave, cadastrar_trecho
from insercoes import cadastrar_voo, cadastrar_reserva
from insercoes import cadastrar_funcionario
from consultas import consultar_clientes, consultar_voos, consultar_aeroportos, consultar_cidades
from consultas import consultar_funcionarios, consultar_trechos, consultar_aeronaves, consultar_reservas
from exclusoes import excluir_cliente, excluir_aeroporto
from exclusoes import excluir_cidade, excluir_aeronave, excluir_trecho, excluir_voo, excluir_funcionario, excluir_aeronave
from alteracoes import atualizar_data_nasc_cliente, atualizar_nome_cliente, atualizar_cidade_aeroporto, atualizar_nome_aeroporto
from alteracoes import atualizar_nome_cidade, atualizar_estado_cidade, atualizar_nome_aeronave, atualizar_poltrona_aeronave
from alteracoes import atualizar_distancia_duracao_trecho, atualizar_origem_destino_trecho, atualizar_preco_trecho
from alteracoes import atualizar_aeronave_trecho_voo, atualizar_data_horario_voo, atualizar_cpf_funcionario, atualizar_nome_funcionario


while True:
    # acrescentar consulta de reservas
    usuario = int(input('Escolha uma opção: \n'
                        '1 - Sou cliente:\n'
                        '2 - Sou funcionário\n'
                        '3 - Sair\n'))

    if usuario == 1:
        while True:
            opcao = int(input('Informe a opção desejada:\n'
                              '1 - Realizar cadastro: \n'
                              '2 - Realizar reserva:\n'
                              '3 - Consultar reservas:\n'
                              '100 - sair\n'))

            if opcao == 1:
                cpf = input('Informe o CPF do cliente: ')
                nome = input('Informe o nome do cliente: ')
                data_nascimento = input('Informe a data de nascimento: ')
                conectar()
                inserir_cliente(cpf, nome, data_nascimento)
                       
                

            elif opcao == 2:
                cpf_cliente = input('Informe o seu cpf: ')
                cpf_funcionario = 000000
                quantidade_passagens = int(input('Informe a quantidade de passagens:'))
                consultar_voos()
                voo_id = int(input('Digite o código do voo: '))
                consultar_trechos()
                trecho_id = int(input('Digite o código do trecho: '))
                cadastrar_reserva(cpf_cliente, cpf_funcionario, quantidade_passagens,voo_id, trecho_id)

            elif opcao == 3:
                cpf_cliente = input('Informe o cpf para consultar a reserva:')
                consultar_reservas(cpf_cliente)
                

            elif opcao == 100:
                print('Saindo..')
                break
            
            else:
                print('Opção inválida')
                break


    elif usuario == 2:

        while True:
            opcao = int(input('Informe a opção desejada:\n'
                              '1 - Realizar cadastros: \n'
                              '2 - Realizar consultas:\n'
                              '3 - Realizar exclusões:\n'
                              '4 - Realizar alterações:\n'                          
                              '100 - sair\n'))

           
            if opcao == 1:
                while True:
                    escolha = int(input('O que você deseja cadastrar: \n'
                                        '1 - Cadastrar clientes\n'
                                        '2 - Cadastrar aeroportos:\n'
                                        '3 - Cadastrar cidades: \n'
                                        '4 - Cadastrar aeronaves:\n'
                                        '5 - Cadastrar trechos: \n'
                                        '6 - Cadastrar voos: \n'
                                        '7 - Cadastrar funcionários: \n'
                                        '100 - Sair \n'))
                    if escolha == 1:
                        cpf = input('Informe o CPF do cliente: ')
                        nome = input('Informe o nome do cliente: ')
                        data_nascimento = input('Informe a data de nascimento: ')
                        conectar()
                        inserir_cliente(cpf, nome, data_nascimento)
                    
                    elif escolha == 2:
                        consultar_cidades()
                        nome_aeroporto = input('Digite o nome do aeroporto: ')
                        cidade_id = input('Digite o codigo da cidade: ')
                        conectar()
                        cadastrar_aeroporto(nome_aeroporto, cidade_id)
                    
                    elif escolha == 3:
                        nome_cidade = input('Digite o nome da cidade: ')
                        estado = input('Digite o Estado: ')
                        conectar()
                        cadastrar_cidade(nome_cidade, estado)
                    
                    elif escolha == 4:
                        nome_aeronave = input('Digite o nome/ tipo da aeronave: ')
                        num_poltronas = input('Digite o numero de poltronas: ')
                        conectar()
                        cadastrar_aeronave(nome_aeronave, num_poltronas)

                    elif escolha == 5:
                        consultar_aeroportos()
                        distancia = input('Digite a distância: ')
                        duracao = input('Digite o tempo de voo: ')
                        preco = int(input('Digite o preço do trecho: '))
                        aeroporto_origem = input('Digite o aeroporto de origem ')
                        aeroporto_destino = input('Digite o aeroporto de destino ')
                        conectar()
                        cadastrar_trecho(distancia, duracao, preco,
                                        aeroporto_origem, aeroporto_destino)
                        
                    elif escolha == 6:
                        consultar_aeronaves()
                        data = input('Informe a data desejada: ')
                        horario = input('Digite o horário: ')
                        aeronave_id = input('Digite o código da aeronave: ')
                        consultar_trechos()
                        trecho_id = input('Digite o código do trecho: ')
                        conectar()
                        cadastrar_voo(data, horario, aeronave_id, trecho_id)

                    elif escolha == 7:
                        cpf = input('Informe o CPF do funcionario: ')
                        nome_funcionario = input('Informe o nome do funcionario: ')
                        conectar()
                        cadastrar_funcionario(cpf, nome_funcionario)

                    elif escolha == 100:
                        print('Saindo...')
                        break

                    else:
                        print('Opção inválida.')
                        break

           
            elif opcao == 2:
                while True:
                    escolha = int(input('O que você deseja consultar: \n'
                                        '1 - Clientes\n'
                                        '2 - Aeroportos:\n'
                                        '3 - Cidades: \n'
                                        '4 - Aeronaves:\n'
                                        '5 - Trechos: \n'
                                        '6 - Voos: \n'
                                        '7 - Funcionários: \n'
                                        '100 - Sair \n')) 
                    
                    if escolha == 1:
                        consultar_clientes()

                    elif escolha == 2:
                        consultar_aeroportos()

                    elif escolha == 3:
                        consultar_cidades()

                    elif escolha == 4: 
                        consultar_aeronaves()
                    
                    elif escolha == 5:
                        consultar_trechos()
                    
                    elif escolha == 6:
                        consultar_voos()
                    
                    elif escolha == 7:
                        consultar_funcionarios()

                    elif escolha == 100:
                        print('Saindo...')
                        break
                    
                    else:
                        print('Opção inválida.')
                        break


                            
            elif opcao == 3:

                while True:
                    escolha = int(input('O que você deseja excluir: \n'
                                        '1 - Clientes\n'
                                        '2 - Aeroportos:\n'
                                        '3 - Cidades: \n'
                                        '4 - Aeronaves:\n'
                                        '5 - Trechos: \n'
                                        '6 - Voos: \n'
                                        '7 - Funcionários: \n'
                                        '100 - Sair \n'))
                    
                    if escolha == 1:
                        consultar_clientes()
                        cpf = input('Digite o CPF do cliente a ser excluído: ')
                        excluir_cliente(cpf)

                
                    elif escolha == 2:
                        consultar_aeroportos()
                        aeroporto_id = int(input('Digite o código do aeroporto a ser excluído: '))
                        excluir_aeroporto(aeroporto_id)

                    elif escolha == 3:
                        consultar_cidades()
                        cidade_id = int(input('Digite o código da cidade a ser excluída: '))
                        excluir_cidade(cidade_id)

                    elif escolha == 4:
                        consultar_aeronaves()
                        aeronave_id = int(input('Digite o código da aeronave a ser excluída: '))
                        excluir_aeronave(aeronave_id)

                    elif escolha == 5:
                        consultar_trechos()
                        trecho_id = int(input('Digite o código do trecho a ser excluído: '))
                        excluir_trecho(trecho_id)

                    elif escolha == 6:
                        consultar_voos()
                        voo_id = int(input('Digite o código do voo a ser excluído: '))
                        excluir_voo(voo_id)

                    elif escolha == 7:
                        consultar_funcionarios()
                        cpf = input('Digite o cpf do funcionário a ser excluído: ')
                        excluir_funcionario(cpf)

                    elif escolha == 100:
                        print('Saindo...')
                        break

                    else:
                        print('Opçao inválida')
                        break

            
            elif opcao == 4:

                 while True:
                    escolha = int(input('O que você deseja alterar: \n'
                                        '1 - Clientes\n'
                                        '2 - Aeroportos:\n'
                                        '3 - Cidades: \n'
                                        '4 - Aeronaves:\n'
                                        '5 - Trechos: \n'
                                        '6 - Voos: \n'
                                        '7 - Funcionários: \n'
                                        '100 - Sair \n'))
                    
                    if escolha == 1:
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

                    elif escolha == 2:
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

                    elif escolha == 3:
                        consultar_cidades()
                        cidade_id = int(input('Digite o código da cidade a ser atualizada: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                            '1 - nome\n'
                                            '2 - estado\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome da cidade: \n')
                            atualizar_nome_cidade(cidade_id, nome)
                        elif atualiza ==2:
                            estado = input('Digite o novo Estado: \n')
                            atualizar_estado_cidade(cidade_id,estado)
                    
                    elif escolha == 4:
                        consultar_aeronaves()
                        aeronave_id = int(input('Digite o código da aeronave a ser atualizada: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                            '1 - nome\n'
                                            '2 - número de poltronas\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome da aeronave: \n')
                            atualizar_nome_aeronave(aeronave_id, nome)
                        elif atualiza ==2:
                            num_poltronas = int(input('Digite o número de poltronas: \n'))
                            atualizar_poltrona_aeronave(aeronave_id,num_poltronas)


                    elif escolha == 5:
                        consultar_trechos()
                        trecho_id = int(input('Digite o código do trecho a ser atualizado: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                            '1 - distancia e duração do trecho:\n'
                                            '2 - origem e destino\n'
                                            '3 - preco\n'))
                        if atualiza == 1:
                            distancia = int(input('Digite o nova distancia: \n'))
                            duracao = input('Digite o tempo de duração do trecho: \n')
                            atualizar_distancia_duracao_trecho(trecho_id, distancia, duracao)
                        elif atualiza == 2:
                            aeroporto_origem = int(input('Digite o código do aeroporto de origem: \n'))
                            aeroporto_destino = int(input('Digite o código do aeroporto de destino: \n'))
                            atualizar_origem_destino_trecho(trecho_id, aeroporto_origem, aeroporto_destino)
                        elif atualiza == 3:
                            preco = int(input('Digite o novo preço: \n'))
                            atualizar_preco_trecho(trecho_id, preco)

                    elif escolha == 6:
                        consultar_voos()
                        voo_id = int(input('Digite o código do voo a ser atualizado: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                            '1 - data e horário do voo:\n'
                                            '2 - aeronave e trecho do voo\n'))
                        if atualiza == 1:
                            data = input('Digite o nova data: \n')
                            horario = input('Digite o horário do voo: \n')
                            atualizar_data_horario_voo(voo_id, data, horario)
                        elif atualiza == 2:
                            aeronave_id = int(input('Digite o código da aeronave: \n'))
                            trecho_id = int(input('Digite o código do trecho: \n'))
                            atualizar_aeronave_trecho_voo(voo_id, aeronave_id, trecho_id)
              
                    elif escolha == 7:
                        consultar_funcionarios()
                        cpf = input('Digite o cpf do funcionário a ser atualizado: ')
                        atualiza = int(input('O que deseja alterar?\n'
                                            '1 - cpf\n'
                                            '2 - nome\n'))
                        if atualiza == 1:
                            novo_cpf = input('Digite o novo cpf do funcionário: \n')
                            atualizar_cpf_funcionario(cpf, novo_cpf)
                        elif atualiza == 2:
                            nome = input('Digite o novo nome do funcionário: \n')
                            atualizar_nome_funcionario(cpf, nome)

                    elif escolha == 100:
                        print('Saindo...')
                        break
                    
                    else:
                        print('Opção inválida...')
                        break
            
            elif opcao == 100:
                print('Saindo...')
                break                             

            else:
                print('Opção inválida.')
                break
                             

    elif usuario == 3:
        print('Saindo...')
        print()
        break

    else:
        print('Opção inválida.')
        print()
        break
