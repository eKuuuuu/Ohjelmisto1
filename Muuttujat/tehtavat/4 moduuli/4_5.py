kayttaja = "python"
salasana = "rules"
i = 0
while True:
    i += 1
    login = input("Anna kayttaja:")
    login2 = input("Anna salasana:")
    if login == kayttaja and login2 == salasana:
        print("Tervetuloa")
        break
    if i == 5:
        print("Pääsy evätty")
        break