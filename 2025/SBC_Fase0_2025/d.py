n = int(input())

s = input()
t = input()
conts = 0
contt = 0
for i in range(n):
    if s[i] == "*":
        conts += 1
    if t[i] == "*":
        contt +=1
result =1- (contt/conts)

print(f"{result:.2f}")
        
