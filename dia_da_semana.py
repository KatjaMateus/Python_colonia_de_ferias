dia = int(input("""Escolhe um número:
                1 = segunda-feira
                2 = terça-feira
                3 = quarta-feira
                4 = quinta-feira
                5 = sexta-feira
                6 = sábado
                7 = domingo 
                """))

if dia == 1:
    print("Segunda-feira")
elif dia == 2:
    print("Terça-feira")
elif dia == 3:
    print("Quarta-feira")
elif dia == 4:
    print("Quinta-feira")
elif dia == 5:
    print("Sexta-feira")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Opção inválida")