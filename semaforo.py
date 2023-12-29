cor = input("""Escolhe uma cor:
            1 = VERMELHO
            2 = AMARELO
            3 = VERDE 
            """)

if cor == "1":
    print("Pare!")
elif cor == "2":
    print("Atenção!")
elif cor == "3":
    print("Acelera!")
else:
    print("Cor inválida!")