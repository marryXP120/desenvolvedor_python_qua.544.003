# importação de biblioteca
import math

# tratamento de exceção
try:
    while True:
        # usuário informa  valor do raio
        r = float(input("informe o valor do raio: ").replace(",","."))

        #  calcula a área do circulo
        area = math.pi*r**2

        # imprime na tela a área do circulo
        print(f"Área do circulo: {area:.2f} m².")

        # usuário informa se deseja continua ou não
        print("1 - calcular ´área de outro circulo")
        print("2 - sair do programa")

        opcao = input("informe sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("opção inválida.")
                continue
except Exception as e:
    print(f"não foi possível calcular. {e}.")