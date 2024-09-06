import random
summa = 0
arpakuutiot = int(input("Monta arpakuutiota on?"))
for i in range(arpakuutiot):
    arpakuutiot = random.randint(1,6)
    summa += arpakuutiot
print("Lopullinen summa", summa)