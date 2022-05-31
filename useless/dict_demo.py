l = ["Soka", "Boka", "Moka", "Koka"]
l1 = ["Soka", "Boka", "Moka", "Koka", "Papska", "Praska", "$iburashka"]

s = zip(l, l1)
print(list(s))


for x, y in zip(l, l1):
    print(x, y)

pari = (12, 33, 12, 33, 44, 55)
dolari = (22, 33, 44, 55, 66, 66)

for e, w in zip(pari, dolari):
    print(e-w)
