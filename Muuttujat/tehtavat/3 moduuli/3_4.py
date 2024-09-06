vuosi = int(input("Anna vuosiluku:"))

if vuosi % 4 & vuosi % 400 == 0:
    print(f"{vuosi} on karkausvosi.")
else:
    print(f"{vuosi} ei ole karkausvosi.")