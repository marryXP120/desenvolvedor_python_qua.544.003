#  tratamento de excecao
try:
    while True:
        nome = input("informe o nome:").strip().title()
        idade= int(input("informea idade:"))
        altura= float(input("informe a altura em metros:").replace(",","."))

        if idade >=12 and altura>= 1.25:
            print(f"{nome}esá liberada.")
        else:
            print(f"entrada de {nome}proibida.")

        print("1-passar novo pagante.")    
        print("2- encerrar programa.")

        opcao= input("informe a opção desejada:").strip()

        match opcao:
            case "1":
                continue
            case "2":
               print("programa encerrado.")
               break
            case _:
                print("opção inválida")
                continue
except:
    print("Não foi possivel registrar a entrada do pagante")