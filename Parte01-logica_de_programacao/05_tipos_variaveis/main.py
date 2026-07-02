# declaracao de vaiaveis
nome = input("informe seu nome: ").title()
idade = int(input("informe sua idade: "))
altura = float(input("informe sua altura em metros: ").replace(",","."))
# saida de dados
print(f"Seu nome é {nome}. {type(nome)}")
print(f"Sua idade é {idade}.{type(idade)}")
