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
                          '2 - Consultar reservas: \n'
                          '3 - Cancelar reservas: \n'
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
