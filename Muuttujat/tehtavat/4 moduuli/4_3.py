arvot = []

while True:
    numero = input("Anna luku:")
    if numero == "":
        break
    arvot.append(numero)
isoin = max(arvot)
pienin = min(arvot)
print(f"Isoin luku on {isoin}")
print(f"Pienin luku on {pienin}")