
#METHOD1
#rotate from outer square to inner
def rotate1(matrix):
    # Do not return anything, modify matrix in-place instead.
    i=0
    n=len(matrix)-1
    while(i<len(matrix)//2):
        for j in range(i,n-i):
            temp=matrix[i][j]
            matrix[i][j]=matrix[n-j][i]
            matrix[n-j][i]=matrix[n-i][n-j]
            matrix[n-i][n-j]=matrix[j][n-i]
            matrix[j][n-i]=temp
        i+=1
        return matrix
    
#METHOD2
#take transpose and reverse each row
def rotate2(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate1(matrix))

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate2(matrix))