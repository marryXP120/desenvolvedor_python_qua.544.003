nomes = ["Fulano", "Citrano", "Beltrano", "João", "Maria", "José"]
nome = input("informe o nome a ser separado: ")
if nome in nomes:
    indice = nomes.index(nome)
else:
    print("nome não encontrado.")
    # separar o nome da lista
    nome_separado = nomes.pop(indice)

# exixte lista
for nome in nomes:
    print(nome)
    print(f"nome separado da lista: {nome_separado}.")
else:
    print("nome não encontrado.")

