summa, nom = map(int, input().split())

summa_kup = 0
kol_vo_kup = 0

nom_kup = []

kup = []
for i in input().split():
    kup.append( int(i) )

kup.sort()
kup.reverse()

for i in range(nom):
    for j in range(2):
        if summa_kup + kup[i] <= summa:
            summa_kup = summa_kup + kup[i]
            kol_vo_kup = kol_vo_kup + 1

            nom_kup.append(kup[i])

if summa == summa_kup:
    print(kol_vo_kup)
    print(" ".join(map(str, nom_kup)))
else:
    print(-1)
