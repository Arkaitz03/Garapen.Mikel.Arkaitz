import egunak
import eragiketa

print("MENUA")
print("=======================")
print("1. Faktoriala")
print("2. Txikiena")
print("3. Hilabetaren Izena")
print("4. Egunaren izena")
print("=======================")
zenb = input("Aukeratu bat: ")

if zenb == 1:
    eragiketa.faktoriala()
elif zenb == 2:
    eragiketa.txikiena()
elif zenb == 3:
    egunak.hilabete_izena()
elif zenb == 4:
    egunak.egun_kopurua()
else:
    print("Ez dago")