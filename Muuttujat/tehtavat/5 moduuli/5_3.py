luku = int(input("Anna alkuluku: "))

prime = True
for i in range(2,luku-1):
    if luku % i == 0:
        prime = False
        break

if prime == True:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")
