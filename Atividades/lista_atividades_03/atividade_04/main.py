# TODO: atividade 04
# utilizando o conceito de modulo, crie um modulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - calcul a potência de um número informado pelo usuário elevado
# a outro numero informado pelo usuário.
# - Calcula a raiz quadrada de um numero informado pelo usuário.
# - calcula o volume de um recipiente paralelepipidico.
# - calcula o volume de um recipiente cilindrico.
# Em seguida, faça um progrma que o usuário escolha executar uma dessas funções ou sair do programa.


import modulo as m

m.limpar()

def main():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1. calcular potencia")
        print("2. calcular raiz quadrada")
        print("3. calcular volume de um recipiente paralelepipidico")
        print("4. calcular volume de recipiente cilindrico")
        print("0. sair do programa")

        opcao = input("escolha uma opção: ").strip()

        if opcao == "1":
            base = float(input("Informe o valor da base: "))
            expoente = float(input("Informe o valor do expoente: "))
            resultado = m.potencia(base, expoente)
            print(f"Resultado: {base}^{expoente} = {resultado} ")

        elif opcao == "2":
           numero = float(input("Informe um numero: "))
           resultado = m.raiz_quadrada(numero)
           print(f"raiz quadrada de: {numero} = {resultado} ")
            
        elif opcao == "3":
           c = float(input("Informe o valor do comprimento: "))
           l = float(input("Informe o valor do largura: "))
           a = float(input("Informe o valor do altura: "))
           resultado = m.calcula_volume_paralelepipedo(c,l,a)
           print(f"O volume é: {resultado} ")

        elif opcao == "4":
           r = float(input("Informe o valor do raio da base: "))
           a = float(input("Informe o valor do altura: "))
           resultado = m.calcula_volume_cilindro(r,a)
           print(f"O volume é: {resultado} ")
 
        elif opcao == "0":
            print("saindo do programa...")
            break

        else:
            print("opção inválida")

if __name__ == "__main__":
    main()

