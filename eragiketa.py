def faktoriala():
    faktoriala = (int(input("Sartu zenbakia:")))
    emaitza = faktoriala * (faktoriala - 1)

    for i in range(faktoriala - 2, 0, -1):
        emaitza = emaitza * i
    print(emaitza)


def txikiena ():
    zerrenda = []
    zenb = int(input("Sartu zenbaki bat: "))
    zerrenda.append(zenb)
    zenb = int(input("Sartu beste zenbaki bat: "))
    zerrenda.append(zenb)
    zenb = int(input("Sartu beste zenbaki bat: "))
    zerrenda.append(zenb)

    print(min(zerrenda) + " txikiena da")
