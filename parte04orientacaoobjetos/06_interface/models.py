from abc import ABC, abstractmethod

class IConta(ABC):
    @abstractmethod
    def consultar_conta():
        pass
    
    @abstractmethod
    def fazer_deposito(valor):
        pass
    
    @abstractmethod
    def fazer_saque(valor):
        pass
    
class Conta(Iconta):
    def __int__(self,titular,cpf,agencia,n_conta,saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__n__conta = n_conta
        self.__saldo = saldo
        
        @property
        def titular(self):
            return self.__titular
        
        @titular.setter
        def titular(self,titular):
            self.__titular = titular
            
@property
def titular(self):
            return self.__titular
        
        @titular.setter def titular(self,titular):
     self.__titular = titula
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     # metodos da interface
     def consultar_conta(selfe):
         print(f"Nome do titular da conta: {self .__titular}")
         print(f"CPF do titular da conta: {self.__cpf}")
         print(f"Agencia da conta: {self.__agencia}")
         print(f"Número da conta: R$ {self.__n__conta}")
         
         
         def fazer_deposito(self,valor):
             self.__ += valor
             return self.__saldo
         
         def fazer_saque(self,valor):
             self.__saldo -= valor
             return self.__saldo           