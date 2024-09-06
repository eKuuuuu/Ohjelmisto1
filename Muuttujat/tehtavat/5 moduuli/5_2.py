lista = []

while True:
    arvo = input("Anna luku: ")
    if arvo == "":
        break
    arvo = int(arvo)
    lista.append(arvo)

lista.sort(reverse=True)
suurimmat = lista[:5] ## Löytöi geeks for geekist

print("Suurimmat luvut ovat:")
for i in suurimmat:
    print(i)

