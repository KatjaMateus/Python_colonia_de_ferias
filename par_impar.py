num = int(input("Digite um número maior que 0: "))
if num <= 0:
    print("Número inválido.")
elif num % 2 == 0:
    print("O número é par")
else:
    print("O número é impar.")