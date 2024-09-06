import random
arpo = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku: "))
    if arvaus == arpo:
        print("Oikein!")
        break
    elif arvaus > arpo:
        print("Liian iso")
    elif arvaus < arpo:
        print("Liian pieni")