import os

from models import PessoaFisica, PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")
    
def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",email="",telefone="",endereco="")
    
    limpar()
    
    # informa os valores o usuario
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o email do usuário: ").strip().lower()
    usuario.telefone = input("Informe o tlefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ")
    
    limpar()
    
    # informa os dados da empresa
    empresa.razao_social = input("Informe o nome juridico da empresa: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ")
    
    # saída de dado
    usuario.exibir_dados()
    empresa.exibir_dados()

if __name__ == "__main__":
    main()



