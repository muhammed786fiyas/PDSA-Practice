
# METHOD1        
def merge1(nums1,m,nums2,n) :    
    
    # Do not return anything, modify nums1 in-place instead.
    
    j=0
    i=m-1
    while (i>=0 and j<n-1):
        if(nums1[i]>nums2[j]):
            nums1[i],nums2[j]=nums2[j],nums1[i]
            i-+1
            j+=1   

        else:
            break
    for i in range(n):
        nums1[m+i]=nums2[i]

    nums1.sort()
    return nums1


# METHOD2
# shell sort -- gap method
def merge2(nums1,m,nums2,n): 
    import math
    for i in range(n):
        nums1[m+i]=nums2[i]

    gap=math.ceil(len(nums1)/2)
    while(1):
        for i in range(gap,len(nums1)):
            if(nums1[i]<nums1[i-gap]):
                nums1[i],nums1[i-gap]=nums1[i-gap],nums1[i]
        if(gap==1):
            break
        gap=math.ceil(gap/2)
    return nums1

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(merge1(nums1,m,nums2,n))

nums1=[1,2,3,5,9,0,0,0,0,0,0,0]
m=5
nums2=[2,4,5,6,8,11,15]
n=7
print(merge2(nums1,m,nums2,n))
