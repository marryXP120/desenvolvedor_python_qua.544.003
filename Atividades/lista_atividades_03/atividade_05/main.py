# TODO: atividade 05
# Usando recursividade, crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência de Fibonacci até o número informado.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("informe um numero: "))

if num < 0:
    print("por favor informe um numero inteiro positivo")
else:
    print(f"Sequência de fibonacci até o termo {num}: ")
    sequencia = [str(fibonacci(i)) for i in range(num + 1)]
    print(",".join(sequencia))
    


 