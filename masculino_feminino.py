sexo = input("""Digite a opção correta: 
             F = feminino
             M = masculino """)
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo inválido")