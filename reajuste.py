salario = float(input("Quanto é o seu salário mensal? "))
if salario < 5000:
    reajuste15 = salario * 1.15
    print(f"Seu salário com o reajuste de 15% é: {reajuste15:.2f}")
elif salario >= 5000 and salario <= 10000:
    reajuste10 = salario * 1.10
    print(f"Seu salário com o reajuste de 10% é: {reajuste10:.2f}")
elif salario > 10000:
    reajuste5 = salario * 1.05
    print(f"Seu salário com o reajuste de 5 % é {reajuste5:.2f}")
