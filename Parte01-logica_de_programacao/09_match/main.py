# entrada de dados
x = float(input("informe o valor de x: ").replace.(",","."))
y = float(input("informe o valor de y: ").replace(",",",".))

# menu
print("1 - Somar")
print("2 - subtrair")
print("3 multiplicar")
print("4 - dividir")

opção = input("informe a opção desejada: ")

match opção:
    case "1":
        print(f"a soma é {x+y}.")
    case "2":
       print(f"a subtração é {x-y}.")
       
        
        
              )