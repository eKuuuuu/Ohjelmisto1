kuukaudet = ("Kevät", "Kesä", "Syksy", "Talvi")

kuukausi = int(input("Anna kuukauden numero:"))

if kuukausi == 1 or kuukausi == 2 or kuukausi == 12:
    print(kuukaudet[3])
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(kuukaudet[0])
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(kuukaudet[1])
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(kuukaudet[2])
else:
    print("Arvon jonka annoit, ei ole kuukausi.")