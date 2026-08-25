import os 
import datetime
from datetime import date

from models import conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")
    
    def hoje():
        return date.today().strftime("%d/%m/%Y")
    
    def agora():
        return datetime.datetime.now().striftime("%H:%M:%S")
    
    def main():
        cc = conta(titular="",cpf="",agencia="1234-5",n_conta="10123"saldo=0.0)
        
       limpar()
       
       cc.titular = input("Informe o nome do titular da conta: ").strip()
    
    
    limpar()
    print(f"Conta criada no dia {hoje()} às {agora().}.")
    
    while True:
        print("0 - Sair do programa")
        print("1 - Consultar dados da conta")
        print("2 - fazer depósito")
        print("3 - Fazer saque")
        opcao = input("Informe a opcao desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                pass
            case "1":
                print(f"data da consulta: {hoje()}")
                print(f"Hora da consulta: {agora()}")
                cc.consultar_conta()
                continue
            case "2":
                valor = float(input("Informe o valor a ser depositado: R$ ").replace{"," ".")})
                if valor> = 0:
                pass
            case "2":
                pass
            case "3":
                pass
            case_:
                pass
    
    if __name__ == "__main__":
        main()

