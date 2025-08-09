def ncr(n,r):
    i=1
    cfact=1
    if r==0:
        return 1
    else:
        while i<=r:
            cfact*=(n-i+1)/i
            i+=1
        return int(cfact)

def pascal_row(n):
    ans=1
    row=[]
    i=1
    while(i<=n):
        row.append(int(ans))
        ans=(ans*(n-i))/i
        i+=1
    return row

# METHOD1
def pascal_triangle_1(n):        
    pt=[]
    for i in range(1,n+1):
        row=pascal_row(i)
        pt.append(row)
    return pt

# METHOD2
def pascal_triangle_2(n):
    pt=[[1]]
    if n==1:
        return pt
    else:
        for i in range(1,n):
            pt.append([1])
            for j in range(1,i):
                pt[i].append(pt[i-1][j-1]+pt[i-1][j])
            pt[i].append(1)
    return pt

print(ncr(10,1))
print(pascal_row(5))
print(pascal_triangle_1(5))
print(pascal_triangle_2(5))





