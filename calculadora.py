num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while True:
    escolha = int(input("""
          Escolha a operação:
          1 = somar
          2 = subtrair
          3 = multiplicar
          4 = dividir
          5 = sair
          """))
    resultado = 0
    if escolha == 1:
        resultado = num1 + num2
    elif escolha == 2:
        resultado = num1 - num2
    elif escolha == 3:
        resultado = num1 * num2
    elif escolha == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:          
            print("Erro! Divisão por 0 não é possível.")
    elif escolha == 5:
        print("Programa encerrado")
        break
    print(f"O resultado é: {resultado}")
