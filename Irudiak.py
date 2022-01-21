def menua():
    zuzena = False
    zenb = 0
    while not zuzena:
        try:
            zenb = int(input("Aukeratu irudi bat: "))
            zuzena = True
        except ValueError:
            print('Zenbaki honek ez du ezer egiten')

    return zenb


irten = False
aukera = 0

while not irten:

    print("1. Laukizuzena")
    print("2. Erronboa")
    print("3. Triangelua")

    aukera = menua()

    if aukera == 1:

        zabalera1 = (int(input("Sartu zabalera: ")))
        altuera = (int(input("Sartu altuera: ")))

        for i in range(1, altuera + 1):
            for j in range(1, zabalera1 + 1):
                print("*", end="")
            print(" ")

    elif aukera == 2:
        zabalera2 = (int(input("Sartu zabalera: ")))


        for p in range(zabalera2):
            print(' ' * (zabalera2 - p - 1) + '* ' * (p + 1))

        for rp in range(zabalera2 - 1, 0, -1):
            print(' ' * (zabalera2 - rp) + '* ' * rp)


    elif aukera == 3:


    else:
        print("Sartu 1-3 tarteko zenbaki bat")

print("Bukaera")
