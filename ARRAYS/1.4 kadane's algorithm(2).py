def maxSubArray(nums):
    sum=0
    maxnum=min(nums)
    for i in range(len(nums)):
        if(sum==0):
            start=i
        sum=sum+nums[i]
        if(sum>maxnum):
            maxnum=sum
            end=i
        if(sum<0):
            sum=0 
    return maxnum,nums[start:end+1] 

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))      