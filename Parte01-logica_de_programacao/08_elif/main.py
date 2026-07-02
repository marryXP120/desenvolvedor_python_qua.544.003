# declaração de variáveis
nome = input('informe o nome do aluno: ').title()
nota = float(input("informe a nota do aluno: ").replace(",","."))

# verifica se a nota é válida
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} esta aprovado.")
    elif nota >= 5:
        print(f"{nome}esta de recuperação.")
else:
    print(f"nota de(nome) invalida.")

