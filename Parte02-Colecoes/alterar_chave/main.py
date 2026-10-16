usuario = {
    'nome': "fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# Usuario informaa chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuario:
    # usuario informa o novo valor para chave
    usuario[chave] = input(f"informe o novo valor para {chave}:").strip()

    # exibe o dicionario com o novo valor da chave escolhida
    for chave, valor in usuario.items():
        for chave, valor in usuario.items():
            print(f"{chave.capitalize()}: {valor}:")

else:
    print("chave não encontrada.")
    
