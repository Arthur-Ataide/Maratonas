letras_obrigatorias = ['E', 'O']
letras_posiçao = [4, 'R']

letras_possives = ['G', 'F', 'R', 'E', 'O', 'J', 'Z', 'K']

consoante = ['G', 'F', 'J', 'Z', 'K']
vogal = ['E', 'O']

palavra = ['_', '_', '_', '_', '_']

for i in range(len(letras_possives)):
    for j in range(len(letras_possives)):
        for k in range(len(letras_possives)):
            for l in range(len(letras_possives)):
                for c in range(len(letras_possives)):
                    palavra = ['_', '_', '_', '_', '_']
                    palavra[0] = letras_possives[i]
                    palavra[1] = letras_possives[j]
                    palavra[2] = letras_possives[k]
                    palavra[3] = letras_possives[l]
                    palavra[4] = letras_possives[c]
                    Erro = 0
                
                    
                    if palavra[0] == 'R' or palavra[0] == 'O' or palavra[1] == 'R' or palavra[2] == 'E' or palavra[-1] == 'G'or palavra[-1] == 'F' or palavra[-1] == 'J' or palavra[-1] == 'K':
                        Erro = 1
                    
                    contE=0
                    contO=0
                    
                    if Erro == 0:
                        for m in range(len(palavra)-1):
                            if Erro == 1:
                                break
                            
                            if palavra[m] == 'E':
                                contE+=1
                            
                            if palavra[m] == 'O':
                                contO+=1
                                
                            if (palavra[m] in consoante and palavra[m+1] in consoante):
                                Erro = 1
                                
                            if (palavra[m+1] == 'R' and palavra[m] in consoante):
                                Erro = 1
                                
                            if (palavra[m+1] == 'R' and palavra[m] =='R'):
                                Erro = 1
                                
                            if m != 3:
                                if (palavra[m] in vogal and palavra[m+1] in vogal and palavra[m+2] in vogal):
                                    Erro = 1
                    if contE == 0 or contO == 0:
                        Erro = 1
                            
                        
                    if Erro == 0:
                        print(palavra)
                    