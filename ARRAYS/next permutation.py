def nextPermutation(nums):
    # modify nums in-place 
    index=-1
    for i in range(len(nums)-2,-1,-1):
        if(nums[i]<nums[i+1]):
            index=i
            break
    if(index==-1):
        nums.reverse()
        return nums
    else:
        for j in range(len(nums)-1,index,-1):
            if(nums[j]>nums[index]):
                nums[j],nums[index]=nums[index],nums[j]
                break
        nums[i+1:]=reversed(nums[i+1:])
        return nums
    
nums=[7,5,6,4,3,2,1]
print(nextPermutation(nums))
