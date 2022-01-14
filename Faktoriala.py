faktoriala = (int(input("Sartu zenbakia:")))
emaitza = faktoriala * (faktoriala-1)

for i in range(faktoriala -2, 0, -1):
    emaitza = emaitza * i
print(emaitza)