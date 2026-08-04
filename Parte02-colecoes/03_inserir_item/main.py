# biblioteca os
import os

# lista vazia
nomes = []

os.system("cls"if os.name == "nt" else "clear")

# loop
while True:
    nome = input("informe um nome:").strip().title()
    # insere nome na lista
    nomes.append(nome)

    print("Deseja inserir mais um nome?")
    print("'s' para sim")
    print("qualquer outro valor para não")
    opcao = input("sua resposta: ")
    os.system("cls" if os.name == "nt" else "clear")
              
    match opcao:
        case "s":
            continue
        case _:
            break
print("lista de nomes:\n")
for name in nomes:
    print(nome)
