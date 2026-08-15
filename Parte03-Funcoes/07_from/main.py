from modulo import limpar, somar, subtrair

def main():
    limpar()
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
    limpar()
    print(f"o valor da soma é : {somar(x, y)}")
    print(f"o valor da subtração é : {subtrair(x, y)}")

if __name__ == "__main__":
    main()

    