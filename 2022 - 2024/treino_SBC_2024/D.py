E, V = map(int, input().split())

H = (E/V) + 19
M = 0
H = H % 24
inteiro = H // 1
resto = E % V
M = (resto/V) * 60

H = int(inteiro)
M = int(M)

print(f"{H:02d}:{M:02d}")

# M = str(int(M))
# H = str(int(inteiro))
# tH = len(H)
# tM =  len(M)

# if tH == 1 and tM==1:   print(f"0{H}:0{M}")
# elif tH == 1:  print(f"0{H}:{M}")
# elif tM == 1:  print(f"{H}:0{M}")
# else:  print(f"{H}:{M}")
