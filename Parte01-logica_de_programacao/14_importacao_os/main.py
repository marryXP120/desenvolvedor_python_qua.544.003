#  importação da biblioteca
import os

#  laço de repetição
while True:
    os.system("cls" if os.name == "nt" else "clear")


    #  entrada de dados
    nome = input("informe o nome: ").strip().title()
    idade = int(input("informe a idade: "))
    cpf = input("informe o cpf: ").strip()
    email = input("informe o email: ").strip().lower()

    os.system("cls" if os.name == "nt" else "clear")

    # saida de dados
    print(f"nome: {nome}.")
    print(f"idade: {idade}.")
    print(f"cpf: {cpf}.")
    print(f"e-mail: {email}.")

    # menu
    print("1 - informar dados de outro usuário")
    print("2 - sair do programa")

    opcao = input("informe a opção desejada: ").strip()

    match opcao:
        case "1":
            continue
        case "2":
            break
        case _:
            print("opção invalida.")
            
    
