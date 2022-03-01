import egunak
import eragiketa


def menu():
    zuzena = False
    zenb = 0
    while not zuzena:
        try:
            zenb = int(input("Aukeratu bat: "))
            zuzena = True
        except ValueError:
            print('Zenbaki honek ez du ezer egiten')

    return zenb

irten = False
aukera = 0

while not irten:
    print("MENUA")
    print("=======================")
    print("0. Irten")
    print("1. Faktoriala")
    print("2. Txikiena")
    print("3. Hilabetaren Izena")
    print("4. Egunaren izena")
    print("5. Irudiak")
    print("=======================")

    aukera = menu()

    if aukera == 1:
        eragiketa.faktoriala()
    elif aukera == 2:
        eragiketa.txikiena()
    elif aukera == 3:
        egunak.hilabete_izena()
    elif aukera == 4:
        egunak.egun_kopurua()
    elif aukera == 5:
        import Irudiak
        Irudiak.menua()
    else:
        print("Sartu 1-5 tarteko zenbaki bat")
print("Bukaera")
