# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# o programa deve calcular a media do aluno e informar se 
# o aluno esta aprovado (media minima =  7) ou reprovado.
# o programa deve gravar esses dados em um json.
# Ao final ,o usuário devera escolher se deseja inserir as
# notas de outro aluno, que deveria ser gravadas no mesmo 
# arquivo json.
import json
import os

os.system("cls" if os.name == "nt" else "clear")


arquivo = "alunos.json"

# Verifica se o arquivo JSON já existe
if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        alunos = json.load(f)
else:
    alunos = []

while True:
    print("\n===== CADASTRO DE ALUNO =====")
            
    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3

    # Verifica a situação
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Cria os dados do aluno
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": round(media, 2),
        "situacao": situacao
    }

    # Adiciona o aluno à lista
    alunos.append(aluno)

    # Grava os dados no arquivo JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)

    print("\n===== RESULTADO =====")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

    # Pergunta se deseja cadastrar outro aluno
    continuar = input("\nDeseja inserir outro aluno? (s/n): ").lower()

    if continuar != "s":
        break

print("\nDados dos alunos gravados com sucesso no arquivo alunos.json!")