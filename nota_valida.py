while True:
    nota = int(input("Dê uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print(int(input("Nota inválida. Dê uma nota entre 0 e 10: "))) 
print(f"Você deu a nota {nota}.")
        