def longestPalindrome(s):
    n = len(s)
    start = 0
    max_len = 1
    
    # dp = [[False for _ in range(n)] for _ in range(n)]

    # for i in range(n):
    #     dp[i][i] = True

    for i in range(1, n-1):
        cont = 1
        
        if max_len//2 + i <= n or i - max_len//2 >= 0:
            tamEsq = i
            tamDir = n-i
            tam = tamEsq
            
            if tamEsq > tamDir:
                tam = tamDir
            
            
            for j in range(1, tam+1):
                print(f"""palavra: {s}
inicio: {s[i]}
comparacao: {s[i-j]} == {s[i+j]}
                      """)
                
                if s[i+j] == s[i-j]:
                    cont +=1
                
            if max_len < cont:
                start = i-j
                max_len = cont
            break
        
    print(s[start])
    print(max_len)
    print(s[start:start+max_len+1])

s = input()

if len(s) == 1:
    print(s)

else:
    longestPalindrome(s)
