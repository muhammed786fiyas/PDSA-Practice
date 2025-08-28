# using merge sort

def merge(arr,left,mid,right):
    inversion=0
    n1=mid-left+1
    n2=right-mid
    l=[0]*n1
    r=[0]*n2

    for i in range(n1):
        l[i]=arr[left+i]
    
    for j in range(n2):
        r[j]=arr[mid+1+j]
    
    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if(l[i]>r[j]):
            arr[k]=r[j]
            j+=1
            inversion += n1-i
        else:
            arr[k]=l[i]
            i+=1
        k+=1
    
    while i<n1:
        arr[k]=l[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k]=r[j]
        j+=1
        k+=1

    return inversion



def merge_sort(arr,left,right):
    inversion=0
    if(left<right):
        mid=(left+right)//2
        inversion+=merge_sort(arr,left,mid)
        inversion+=merge_sort(arr,mid+1,right)
        inversion+=merge(arr,left,mid,right)
    return inversion


def no_of_inversion(arr):
    inversion=0
    left=0
    right=len(arr)-1
    return merge_sort(arr,left,right)

arr=[4,5,7,3,2,1]
print(no_of_inversion(arr),arr)


