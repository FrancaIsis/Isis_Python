import os
import sqlite3
import exclusoes
import alteracoes
import conexao
import consultas
import insercoes
import guia_cliente


def main():
    print('-'*70)
    print('Bem vindo a Isis SkyLine!')
    print('-'*70)

    while True:
        usuario = int(input('Escolha a plataforma que deseja utilizar: \n'
                            '1 - Sou cliente:\n'
                            '2 - Sou funcionário\n'
                            '3 - Sair\n'))
        if usuario == 1:
            os.system('cls')
            guia_cliente.menu_cliente()
            # chamar função com menu do usuario

        elif usuario == 2:
            os.system('cls')
            pass
            # chamar função com menu do funcionario

        elif usuario == 3:
            os.system('cls')
            print('Obrigado por nos visitar!')
            break
        else:
            input('Opção inválida, pressione Enter para sair.')
            break


if __name__ == "__main__":
    main()
