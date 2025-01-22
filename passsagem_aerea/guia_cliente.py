import os
import sqlite3
import exclusoes
import alteracoes
import conexao
import consultas
import insercoes


def menu_cliente():
    cpf = input('Informe seu cpf (somente números):').strip()

    conn = conexao.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome_cliente FROM clientes WHERE cpf = ?", (cpf,))
    resultados = cursor.fetchall()

    # verificando se o cliente já é cadastrado.
    if not resultados:
        print('Seja bem vindo ao nosso site!')
        cpf = input('Informe o CPF do cliente: ')
        nome = input('Informe o nome do cliente: ')
        data_nascimento = input('Informe a data de nascimento: ')
        insercoes.inserir_cliente(cpf, nome, data_nascimento)
    else:
        print(f'Bem vindo de volta {resultados}')

    while True:
        opcao = int(input('O que você deseja?\n'
                          '1 - Visualizar destinos: \n'
                          '2 - Consultar reservas: \n'#ok
                          '3 - Cancelar reservas: \n' #ok
                          '4 - Atualizar cadastro: \n'
                          '5 - Retornar ao menu anterior, \n'))
        if opcao == 1:
            os.system('cls')
            # chamar alguma função que mostre os destinos com os preços e datas/ horarios
            pass

        elif opcao == 2:
            os.system('cls')
            consultas.consultar_reservas(cpf)

        elif opcao == 3:
            # os.system('cls')
            consultas.consultar_reservas(cpf)
            reserva_id = int(
                input('Digite o código da reserva a ser excluída: '))
            exclusoes.excluir_reserva(reserva_id)
        
        elif opcao == 4:
            os.system('cls')
            consultas.consultar_clientes_por_cpf(cpf)
            while True:
                atualiza = int(input('O que deseja alterar?\n'
                                    '1 - nome\n'
                                    '2 - data de nascimento\n'
                                    '3 - CPF\n'
                                    '4 - Retornar ao menu anterior\n'))
                if atualiza == 1:
                    nome = input('Digite o nome correto: \n')
                    alteracoes.atualizar_nome_cliente(cpf, nome)
                    consultas.consultar_clientes_por_cpf(cpf)
                
                elif atualiza == 2:
                    data_nascimento = input(
                    'Digite a data de nascimento correta: \n')
                    alteracoes.atualizar_data_nasc_cliente(
                                    cpf, data_nascimento)
                    consultas.consultar_clientes_por_cpf(cpf)
                elif atualiza == 3:
                    novo_cpf = input('Digite o CPF correto: \n')
                    alteracoes.atualizar_cpf_cliente(novo_cpf,cpf)
                    consultas.consultar_clientes_por_cpf(novo_cpf)
                
                elif atualiza == 4:
                    print('Saindo...')
                    break
                else:
                    input('Opção inválida.')
