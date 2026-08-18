# TODO: atividade 04
# utilizando o conceito de modulo, crie um modulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - calcul a potência de um número informado pelo usuário elevado
# a outro numero informado pelo usuário.
# - Calcula a raiz quadrada de um numero informado pelo usuário.
# - calcula o volume de um recipiente paralelepipidico.
# - calcula o volume de um recipiente cilindrico.
# Em seguida, faça um progrma que o usuário escolha executar uma dessas funções ou sair do programa.


import modulo as m

m.limpar()

def main():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1. calcular potencia")
        print("2. calcular raiz quadrada")
        print("3. calcular volume de um recipiente paralelepipidico")
        print("4. calcular volume de recipiente cilindrico")
        print("0. sair do programa")

        opcao = input("escolha uma opção: ").strip()

        if opcao == "1":
            base = float(input)
            m.potencia()

        elif opcao == "2":
            m.raiz_quadrada()

        elif opcao == "3":
            m.calcula_volume_paralelepipedo()

        elif opcao == "4":
            m.calcula_volume_cilindro()

        elif opcao == "0":
            print("saindo do programa...")
            break

        else:
            print("opção inválida")

if __name__ == "__main__":
    main()

