from abc import ABC, abstractmethod
from dataclasses import dataclass


class IConta(ABC):  
    @abstractmethod
    def consultar_dados(self):
        pass
    
    @abstractmethod
    def gerar_extrato():
        pass
    
    @abstractmethod
    def fazer_deposito(valor: float):
        pass
    
    @abstractmethod
    def fazer_saque(valor: float):
        pass
    
# Classe Pessoa com dataclass
@dataclass
class Pessoa:
    nome: str
    cpf: str
    
    def __str__(self):
        return f"Titular: {self.nome} | CPF: {self.cpf}"
    
    
# Classe Conta implementando IConta 
@dataclass
class Conta(IConta):
    titular: Pessoa
    agencia: str
    n_conta: str
    saldo: float
    
    def consultar_dados(self):
        print("Dados da conta")
        print(self.titular)
        print(f"Agencia: {self.agencia}")
        print(f"Conta: {self.n_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        
    def fazer_deposito(self, valor: float):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        
        
    def fazer_saque(self,valor: float):
        self.saldo -= valor
        print(f"saque de R$ {valor:.2f} realizado com sucesso")
        
        
    def gerar_extrato(self):
        nome_arquivo = f"extrato_{self.n_conta}.txt"
        conteudo = (
            f" EXTRATO BANCÁRIO \n"
            f"Nome: {self.titular.nome}\n"
            f"CPF: {self.titular.cpf}\n"
            f"Agencia: {self.agencia}\n"
            f"Conta: {self.n_conta}\n"
            f"Saldo Atual: R$ {self.saldo:.2f}\n"
        )
        
    with open(nome_arquivo, "w" , encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
        
        print(f"Extrato gerado com sucesso no arquivo '{nome_arquivo}'.") 
    
    
    
     
    

