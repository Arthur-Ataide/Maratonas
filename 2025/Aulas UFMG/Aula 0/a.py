n = int(input())
result = 1

for i in range(2, n+1):
    f = int(str(i)[-1])
    if (f != 2 and f != 5 and f != 0):
        result *= i

print(result)
