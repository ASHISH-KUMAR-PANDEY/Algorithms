import math as mt 
  
# Size of given matrix is N X N 
N = 6
  
# A utility function to find minimum 
# of two numbers 
def getMin(x, y): 
    if x < y: 
        return x 
    else: 
        return y 
          
# Returns size of Maximum size  
# subsquare matrix surrounded by 'X' 
def findSubSquare(mat): 
  
    Max = 0 # Initialize result 
  
    # Initialize the left-top value  
    # in hor[][] and ver[][] 
    hor = [[0 for i in range(N)]  
              for i in range(N)] 
    ver = [[0 for i in range(N)]  
              for i in range(N)] 
  
    if mat[0][0] == 'X': 
        hor[0][0] = 1
        ver[0][0] = 1
  
    # Fill values in hor[][] and ver[][] 
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
  
    # Start from the rightmost-bottommost corner  
    # element and find the largest ssubsquare 
    # with the help of hor[][] and ver[][] 
    for i in range(N - 1, 0, -1): 
      
        for j in range(N - 1, 0, -1): 
          
            # Find smaller of values in hor[][] and  
            # ver[][]. A Square can only be made by  
            # taking smaller value 
            small = getMin(hor[i][j], ver[i][j]) 
  
            # At this point, we are sure that there  
            # is a right vertical line and bottom  
            # horizontal line of length at least 'small'. 
  
            # We found a bigger square if following  
            # conditions are met: 
            # 1)If side of square is greater than Max. 
            # 2)There is a left vertical line  
            #   of length >= 'small' 
            # 3)There is a top horizontal line  
            #   of length >= 'small' 
            while (small > Max): 
              
                if (ver[i][j - small + 1] >= small and 
                    hor[i - small + 1][j] >= small): 
                  
                    Max = small 
                  
                small -= 1
              
    return Max
  
# Driver Code 
mat = [['X', 'O', 'X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X', 'O', 'X'], 
       ['X', 'X', 'X', 'O', 'O', 'X'], 
       ['O', 'X', 'X', 'X', 'X', 'X'], 
       ['X', 'X', 'X', 'O', 'X', 'O'], 
       ['O', 'O', 'X', 'O', 'O', 'O']] 
print(findSubSquare(mat)) 
