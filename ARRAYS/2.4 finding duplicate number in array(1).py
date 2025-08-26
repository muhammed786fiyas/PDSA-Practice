def findDuplicate(nums):
    # Good problem uses linked list cycle method
    slow=nums[0]
    fast=nums[0]
    while(1):
        slow=nums[slow]
        fast=nums[nums[fast]]
        if(slow==fast):
            break
    fast=nums[0]
    while(slow!=fast):
        slow=nums[slow]
        fast=nums[fast]
    
    return slow

nums=[1,2,3,4,2]
print(findDuplicate(nums))