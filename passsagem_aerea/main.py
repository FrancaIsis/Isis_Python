import os
import sqlite3
import exclusoes
import alteracoes
import conexao
import consultas
import insercoes


while True:
    # acrescentar consulta de reservas
    usuario = int(input('Escolha uma opção: \n'
                        '1 - Sou cliente:\n'
                        '2 - Sou funcionário\n'
                        '3 - Sair\n'))

    if usuario == 1:
        os.system('cls')

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
                conexao.conectar()
                insercoes.inserir_cliente(cpf, nome, data_nascimento)

            elif opcao == 2:
                cpf_cliente = input('Informe o seu cpf: ')
                cpf_funcionario = 000000
                quantidade_passagens = int(
                    input('Informe a quantidade de passagens:'))
                consultas.consultar_voos()
                voo_id = int(input('Digite o código do voo: '))
                consultas.consultar_trechos()
                trecho_id = int(input('Digite o código do trecho: '))
                insercoes.cadastrar_reserva(cpf_cliente, cpf_funcionario,
                                            quantidade_passagens, voo_id, trecho_id)

            elif opcao == 3:
                cpf_cliente = input('Informe o cpf para consultar a reserva:')
                consultas.consultar_reservas(cpf_cliente)

            # elif opcao == 100:
            #     print('Saindo..')
            #     break
            
            else:
                input('Pressione enter para retornar ao menu anterior.')
                print()
                break
            

    elif usuario == 2:
        os.system('cls')
        while True:
            opcao = int(input('Informe a opção desejada:\n'
                              '1 - Realizar cadastros: \n'
                              '2 - Realizar consultas:\n'
                              '3 - Realizar exclusões:\n'
                              '4 - Realizar alterações:\n'
                              '100 - sair\n'))

            if opcao == 1:
                os.system('cls')
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
                        os.system('cls')
                        cpf = input('Informe o CPF do cliente: ')
                        nome = input('Informe o nome do cliente: ')
                        data_nascimento = input(
                            'Informe a data de nascimento: ')
                        conexao.conectar()
                        insercoes.inserir_cliente(cpf, nome, data_nascimento)

                    elif escolha == 2:
                        os.system('cls')
                        consultas.consultar_cidades()
                        nome_aeroporto = input('Digite o nome do aeroporto: ')
                        cidade_id = input('Digite o codigo da cidade: ')
                        conexao.conectar()
                        insercoes.cadastrar_aeroporto(
                            nome_aeroporto, cidade_id)

                    elif escolha == 3:
                        os.system('cls')
                        nome_cidade = input('Digite o nome da cidade: ')
                        estado = input('Digite o Estado: ')
                        conexao.conectar()
                        insercoes.cadastrar_cidade(nome_cidade, estado)

                    elif escolha == 4:
                        os.system('cls')
                        nome_aeronave = input(
                            'Digite o nome/ tipo da aeronave: ')
                        num_poltronas = input('Digite o numero de poltronas: ')
                        conexao.conectar()
                        insercoes.cadastrar_aeronave(
                            nome_aeronave, num_poltronas)

                    elif escolha == 5:
                        os.system('cls')
                        consultas.consultar_aeroportos()
                        distancia = input('Digite a distância: ')
                        duracao = input('Digite o tempo de voo: ')
                        preco = int(input('Digite o preço do trecho: '))
                        aeroporto_origem = input(
                            'Digite o aeroporto de origem ')
                        aeroporto_destino = input(
                            'Digite o aeroporto de destino ')
                        conexao.conectar()
                        insercoes.cadastrar_trecho(distancia, duracao, preco,
                                                   aeroporto_origem, aeroporto_destino)

                    elif escolha == 6:
                        os.system('cls')
                        consultas.consultar_aeronaves()
                        data = input('Informe a data desejada: ')
                        horario = input('Digite o horário: ')
                        aeronave_id = input('Digite o código da aeronave: ')
                        consultas.consultar_trechos()
                        trecho_id = input('Digite o código do trecho: ')
                        conexao.conectar()
                        insercoes.cadastrar_voo(
                            data, horario, aeronave_id, trecho_id)

                    elif escolha == 7:
                        os.system('cls')
                        cpf = input('Informe o CPF do funcionario: ')
                        nome_funcionario = input(
                            'Informe o nome do funcionario: ')
                        conexao.conectar()
                        insercoes.cadastrar_funcionario(cpf, nome_funcionario)

                    # elif escolha == 100:
                    #     print('Saindo...')
                    #     break

                    else:
                        input('Pressione enter para retornar ao menu anterior.')
                        print()
                        break

            elif opcao == 2:
                os.system('cls')
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
                        os.system('cls')
                        consultas.consultar_clientes()

                    elif escolha == 2:
                        os.system('cls')
                        consultas.consultar_aeroportos()

                    elif escolha == 3:
                        os.system('cls')
                        consultas.consultar_cidades()

                    elif escolha == 4:
                        os.system('cls')
                        consultas.consultar_aeronaves()

                    elif escolha == 5:
                        os.system('cls')
                        consultas.consultar_trechos()

                    elif escolha == 6:
                        os.system('cls')
                        consultas.consultar_voos()

                    elif escolha == 7:
                        os.system('cls')
                        consultas.consultar_funcionarios()

                    # elif escolha == 100:
                    #     print('Saindo...')
                    #     break

                    else:
                        input('Pressione enter para retornar ao menu anterior.')
                        print()
                        break
                        

            elif opcao == 3:
                os.system('cls')

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
                        os.system('cls')
                        consultas.consultar_clientes()
                        cpf = input('Digite o CPF do cliente a ser excluído: ')
                        exclusoes.excluir_cliente(cpf)

                    elif escolha == 2:
                        os.system('cls')
                        consultas.consultar_aeroportos()
                        aeroporto_id = int(
                            input('Digite o código do aeroporto a ser excluído: '))
                        exclusoes.excluir_aeroporto(aeroporto_id)

                    elif escolha == 3:
                        os.system('cls')
                        consultas.consultar_cidades()
                        cidade_id = int(
                            input('Digite o código da cidade a ser excluída: '))
                        exclusoes.excluir_cidade(cidade_id)

                    elif escolha == 4:
                        os.system('cls')
                        consultas.consultar_aeronaves()
                        aeronave_id = int(
                            input('Digite o código da aeronave a ser excluída: '))
                        exclusoes.excluir_aeronave(aeronave_id)

                    elif escolha == 5:
                        os.system('cls')
                        consultas.consultar_trechos()
                        trecho_id = int(
                            input('Digite o código do trecho a ser excluído: '))
                        exclusoes.excluir_trecho(trecho_id)

                    elif escolha == 6:
                        os.system('cls')
                        consultas.consultar_voos()
                        voo_id = int(
                            input('Digite o código do voo a ser excluído: '))
                        exclusoes.excluir_voo(voo_id)

                    elif escolha == 7:
                        os.system('cls')
                        consultas.consultar_funcionarios()
                        cpf = input(
                            'Digite o cpf do funcionário a ser excluído: ')
                        exclusoes.excluir_funcionario(cpf)

                    # elif escolha == 100:
                    #     print('Saindo...')
                    #     break

                    else:
                        input('Pressione enter para retornar ao menu anterior.')
                        print()
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
                        consultas.consultar_clientes()
                        cpf = input(
                            'Digite o cpf do cliente a ser atualizado: ')
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - nome\n'
                                             '2 - data de nascimento\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome do cliente: \n')
                            alteracoes.atualizar_nome_cliente(cpf, nome)
                        elif atualiza == 2:
                            data_nascimento = input(
                                'Digite a data de nascimento correta: \n')
                            atualizar_data_nasc_cliente(cpf, data_nascimento)

                    elif escolha == 2:
                        consultas.consultar_aeroportos()
                        aeroporto_id = int(
                            input('Digite o código do aeroporto a ser atualizado: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - nome\n'
                                             '2 - cidade\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome do aeroporto: \n')
                            alteracoes.atualizar_nome_aeroporto(
                                aeroporto_id, nome)
                        elif atualiza == 2:
                            cidade_id = int(
                                input('Digite o código da cidade correta: \n'))
                            alteracoes.atualizar_cidade_aeroporto(
                                aeroporto_id, cidade_id)

                    elif escolha == 3:
                        consultas.consultar_cidades()
                        cidade_id = int(
                            input('Digite o código da cidade a ser atualizada: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - nome\n'
                                             '2 - estado\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome da cidade: \n')
                            alteracoes.atualizar_nome_cidade(cidade_id, nome)
                        elif atualiza == 2:
                            estado = input('Digite o novo Estado: \n')
                            alteracoes.atualizar_estado_cidade(
                                cidade_id, estado)

                    elif escolha == 4:
                        consultas.consultar_aeronaves()
                        aeronave_id = int(
                            input('Digite o código da aeronave a ser atualizada: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - nome\n'
                                             '2 - número de poltronas\n'))
                        if atualiza == 1:
                            nome = input('Digite o novo nome da aeronave: \n')
                            alteracoes.atualizar_nome_aeronave(
                                aeronave_id, nome)
                        elif atualiza == 2:
                            num_poltronas = int(
                                input('Digite o número de poltronas: \n'))
                            alteracoes.atualizar_poltrona_aeronave(
                                aeronave_id, num_poltronas)

                    elif escolha == 5:
                        consultas.consultar_trechos()
                        trecho_id = int(
                            input('Digite o código do trecho a ser atualizado: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - distancia e duração do trecho:\n'
                                             '2 - origem e destino\n'
                                             '3 - preco\n'))
                        if atualiza == 1:
                            distancia = int(
                                input('Digite o nova distancia: \n'))
                            duracao = input(
                                'Digite o tempo de duração do trecho: \n')
                            alteracoes.atualizar_distancia_duracao_trecho(
                                trecho_id, distancia, duracao)
                        elif atualiza == 2:
                            aeroporto_origem = int(
                                input('Digite o código do aeroporto de origem: \n'))
                            aeroporto_destino = int(
                                input('Digite o código do aeroporto de destino: \n'))
                            alteracoes.atualizar_origem_destino_trecho(
                                trecho_id, aeroporto_origem, aeroporto_destino)
                        elif atualiza == 3:
                            preco = int(input('Digite o novo preço: \n'))
                            alteracoes.atualizar_preco_trecho(trecho_id, preco)

                    elif escolha == 6:
                        consultas.consultar_voos()
                        voo_id = int(
                            input('Digite o código do voo a ser atualizado: '))
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - data e horário do voo:\n'
                                             '2 - aeronave e trecho do voo\n'))
                        if atualiza == 1:
                            data = input('Digite o nova data: \n')
                            horario = input('Digite o horário do voo: \n')
                            alteracoes.atualizar_data_horario_voo(
                                voo_id, data, horario)
                        elif atualiza == 2:
                            aeronave_id = int(
                                input('Digite o código da aeronave: \n'))
                            trecho_id = int(
                                input('Digite o código do trecho: \n'))
                            alteracoes.atualizar_aeronave_trecho_voo(
                                voo_id, aeronave_id, trecho_id)

                    elif escolha == 7:
                        consultas.consultar_funcionarios()
                        cpf = input(
                            'Digite o cpf do funcionário a ser atualizado: ')
                        atualiza = int(input('O que deseja alterar?\n'
                                             '1 - cpf\n'
                                             '2 - nome\n'))
                        if atualiza == 1:
                            novo_cpf = input(
                                'Digite o novo cpf do funcionário: \n')
                            alteracoes.atualizar_cpf_funcionario(cpf, novo_cpf)
                        elif atualiza == 2:
                            nome = input(
                                'Digite o novo nome do funcionário: \n')
                            alteracoes.atualizar_nome_funcionario(cpf, nome)

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
