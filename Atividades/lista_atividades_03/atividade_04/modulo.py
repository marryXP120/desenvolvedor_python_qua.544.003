import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def potencia(numero, expoente):    
    return numero ** expoente 
       
def raiz_quadrada(numero):
    if numero < 0:
        return None
    return math.sqrt(numero)

def calcula_volume_paralelepipedo(c, l, a):
    return c*l*a

def calcula_volume_cilindro(r, a):
    return math.pi * (r**2) * a
    



