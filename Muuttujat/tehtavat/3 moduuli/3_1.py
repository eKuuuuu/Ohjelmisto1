kuha = int(input("Anna kuhaan pituus: "))
if kuha <= 36:
    print(f"Laske kuha takaisin veteen, kuhan minimi pituudesta puuttuu {37 - kuha} sentimettriä")
else:
    print(f"{kuha} sentimettriä pitkä on hyväksyttävä")
