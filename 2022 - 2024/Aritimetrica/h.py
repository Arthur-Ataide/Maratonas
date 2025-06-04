N = int(input())
aves = input().split()
conta = 0
for c in range(N):
    conta += int(aves[c])
print("{:.2f}".format(conta/N))
