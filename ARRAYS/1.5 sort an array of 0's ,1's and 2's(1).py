
def sortColors(nums):
    
    # Do not return anything, modify nums in-place instead.
    # The algorith used is Dutch national flag algorithm
   
    low=0
    mid=0
    high=len(nums)-1

    while(mid<=high):
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

nums=[0,1,2,2,1,2,0,0,0,1,2,2,2,1,1]
print(sortColors(nums))