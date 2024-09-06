laivaluokka = input("Anna hyttiluokka: ")
laivaluokka = laivaluokka.upper()

if laivaluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laivaluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laivaluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif laivaluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
##elif laivaluokka != "LUX" or "A" or "B" or "C":
else:
    print("Virheellinen hyttiluokka")