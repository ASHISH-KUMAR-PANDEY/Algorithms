import math as mt  
N = 6

def getMin(x, y): 
    if x < y: 
        return x 
    else: 
        return y 

def findSubSquare(mat): 
  
    Max = 0 
 
    hor = [[0 for i in range(N)]  
              for i in range(N)] 
    ver = [[0 for i in range(N)]  
              for i in range(N)] 
  
    if mat[0][0] == 'X': 
        hor[0][0] = 1
        ver[0][0] = 1

    for i in range(N): 
      
        for j in range(N): 
          
            if (mat[i][j] == 'O'): 
                ver[i][j], hor[i][j] = 0, 0
            else: 
                if j == 0: 
                    ver[i][j], hor[i][j] = 1, 1
                else: 
                    (ver[i][j],  
                     hor[i][j]) = (ver[i - 1][j] + 1,  
                                   hor[i][j - 1] + 1) 

    for i in range(N - 1, 0, -1): 
      
        for j in range(N - 1, 0, -1): 

            small = getMin(hor[i][j], ver[i][j]) 
  
            while (small > Max): 
              
                if (ver[i][j - small + 1] >= small and 
                    hor[i - small + 1][j] >= small): 
                  
                    Max = small 
                  
                small -= 1
              
    return Max
  
mat = [['X', 'O', 'X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X', 'O', 'X'], 
       ['X', 'X', 'X', 'O', 'O', 'X'], 
       ['O', 'X', 'X', 'X', 'X', 'X'], 
       ['X', 'X', 'X', 'O', 'X', 'O'], 
       ['O', 'O', 'X', 'O', 'O', 'O']] 
print(findSubSquare(mat)) 
