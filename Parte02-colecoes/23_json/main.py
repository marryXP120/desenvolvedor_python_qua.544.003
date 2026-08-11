import json
import os

usuarios = []
abrir =""

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Gravar novo arquivo json")
    print("2 - Gravar em arquivo json existente")
    print("3 - ler arquivo json")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if opcao == "1" or opcao == "2":
    usuario = {} 
    usuario['nome'] = input("informe o nome: ").strip().title
    usuario['email'] = input("Informe o e-mail:" ).strip().lower

    usuarios.append(usuario)

    match opcao:
        case "1":
            arquivo = input("Informe o nome do arquivo: ")

            with open(f"23_json\{arquivo}.json","w", encoding="utf-8") as f:
                json.dump(usuarios, f)
                case "2":
                if abrir:  "abrir" não esta definido
                with open(f"23_json\{abrir}.json","w", encoding="utf-8") as f:
                    json.dump(usuarios,f)
else:
            match opcao:
                  case "3":
                        abrir = input("Informe o nome do aruivo que deseja abrir: ")

                        with open(f"23_json\{abrir}")
                  case "4":
                        break
                  case_:
            print("opção inválida.")
            continu