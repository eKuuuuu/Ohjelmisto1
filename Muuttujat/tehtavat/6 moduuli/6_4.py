import random
luvut = []
def summa(lista):
    summa = sum(lista)
    return (f"Listan summa on: {summa}")

for i in range(10):
    x = random.randint(1,10)
    luvut.append(x)

print(summa(luvut))