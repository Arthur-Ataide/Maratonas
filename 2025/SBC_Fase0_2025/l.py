import math

entrada = int(input())

valor = entrada *8* 10**6 

saida = math.log2(valor)

print(math.ceil(saida))