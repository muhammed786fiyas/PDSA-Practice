def setZeroes(matrix):
    # modify matrix in-place 
    col0=1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                if(j==0):
                    col0=0
                    matrix[i][0]=0
                else:
                    matrix[i][0]=0
                    matrix[0][j]=0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if(matrix[i][0]==0 or matrix[0][j]==0):
                matrix[i][j]=0
    for j in range(1,len(matrix[0])):
        if matrix[0][0]==0:
            matrix[0][j]=0
    for i in range(len(matrix)):
        if col0==0:
            matrix[i][0]=0
    
    return matrix
    
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))