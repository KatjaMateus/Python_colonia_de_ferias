num = int(input("Digite um número maior que 0: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"O número {num} é divisível por 3 e por 5.")
else:
    print("O número não é divisível por 3 e por 5")