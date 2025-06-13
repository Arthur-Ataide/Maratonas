cont = 0

try:
    while(1):

        cont+=1
        n = int(input())
        result = 1

        for i in range(2, n+1):
            result *= i
        
        for i in str(result)[::-1][n//5:]:
            if i != "0":
                print("Instancia", cont)
                print(result)
                print(i)
                break
except EOFError:
    exit(0)