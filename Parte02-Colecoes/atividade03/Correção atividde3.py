import os
import json

alunos = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1- Informa dados")
    print("2- sair do programa")
    opcao = input("Informe a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            aluno = {}
            notas = [0,0,0]
            aluno['nome'] = input("Informe o nom do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i]= float(input(f"Informe a {i+1}ª nota: ").replace(",","."))
                aluno['notas'] = notas
                aluno['média'] = sum(notas)/len(notas)
                aluno['resultado'] = "aprovado" if aluno['média'] >= 7 else "reprovado"
                alunos.append(aluno)
                with open(f"atividade03/alunos.json","w", encoding="utf-8") as f:
                    json.dump(alunos, f)
                print("Dados do aluno gravados com sucesso!")
                continue
        case "2":
            break
        case _:
            print("Opção inválida")
            continue
            

