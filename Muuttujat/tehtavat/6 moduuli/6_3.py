def gallonit_litroina(gallonit):
    litrat = gallonit *  3.785
    return litrat

def kayttaja():
    while True:
        gallon = float(input("Anna bensan määrä galloneina: "))

        if gallon < 0:
            break

        litrat = gallonit_litroina(gallon)

        print(f"{gallon} gallonaa on {litrat:.2f} litroina.")

kayttaja()