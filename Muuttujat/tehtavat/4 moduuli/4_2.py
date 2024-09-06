while True:
    luku = float(input("Anna tuumien määrä: "))
    if luku <= 0:
        print("Ohjelma loppuu")
        break
    else:
        print(f"Tuumien määrä on {(luku*2.54):2f} sentimetriä")