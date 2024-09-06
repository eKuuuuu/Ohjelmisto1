import random

def jaolliset_kahdella(lista):
    luvut2 = []
    for i in lista:
        if i % 2 == 0:
            luvut2.append(i)
    return luvut2

luvut = []
for i in range(10):
    x = random.randint(1,10)
    luvut.append(x)

print(jaolliset_kahdella(luvut))