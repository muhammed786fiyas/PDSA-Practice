#METHOD 1 : mathematical
def findMissingRepeatingNumbers1(nums):
    n=len(nums)
    
    sum_list=sum(nums)
    sum_n=(n*(n+1))//2
    xr=sum_list-sum_n  #xr=a-b
    
    sq_nums=[xr**2 for xr in nums]
    sq_nums_sum=sum(sq_nums)
    sq_sum_n=(n*(n+1)*((2*n)+1))//6
    y=(sq_nums_sum-sq_sum_n)//xr
    
    a=(y+xr)//2
    b=(y-xr)//2

    return [a,b]

#METHOD 2 : using bitwise XOR
# order doesn't matter in bitwise or
''' 
basically we dividing nums=[4,3,6,2,5,5],list_n[1,2,3,4,5,6] as [1,1,1,2,2,3,3],[4,4,5,6,6,]
for that we xor all elements of nums and list_n and every thing cancels and only 1^5=4 remains
so we decide our partition based on the first bit that is one in our xor.
incase of 4(0b100) the third bit from right is first bit that is 1" 
so we divide the array nums,list_n based on (0b100), all numbers with their 3rd bit zero will be in zero_club. 
and all numbers with their 3rd bit one will be in one_club. ather this we get missing number and repeating number in diff lists
then we finally do bitwise or on both array seperately so we get missing and repeated no. of elements in either of the lists
since these element occur odd no of times and all other elements will cancel out sice they occur even no of times 

'''
# actually we are not storing the partitioned elements in seperate arrays, we do bitwise or(^) on the go so that we can save space

def findMissingRepeatingNumbers2(nums):
    n=len(nums)
    list_n=[i+1 for i in range(n)]
    xr=0
    for i in range(n):
        xr=xr ^ nums[i]
        xr=xr ^ list_n[i]

    bitno=0
    while(1):
        if(xr & (1<<bitno)!=0):
            break
        bitno+=1
    
    zero_culb=0
    one_club=0

    for i in range(n):
        if((nums[i]&(1<<bitno))!=0):
            one_club^=nums[i]
        else:
            zero_culb^=nums[i]

        if((list_n[i]&(1<<bitno))!=0):
            one_club^=list_n[i]
        else:
            zero_culb^=list_n[i]
        
    if(zero_culb in nums):
        a,b=zero_culb,one_club
    else:
        a,b=one_club,zero_culb


    return[a,b]
    
   
# Example usage:
nums =  [4,3,6,2,5,5]
print(findMissingRepeatingNumbers1(nums))
print(findMissingRepeatingNumbers2(nums)) 



