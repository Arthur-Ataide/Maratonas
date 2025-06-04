pala = input()
al = []
oi = []

for i in range(1, len(pala)+1):
     al.append(pala[len(pala) - i])
     oi.append(pala[i-1])


if al == oi:
    print('sim')

else:
    print('nao')