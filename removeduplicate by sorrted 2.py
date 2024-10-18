def rd():
    nums=[1,1]
    i=2
    
    while i < len(nums):
        if nums[i]==nums[i-1]==nums[i-2]:
            nums.pop(i)
        
        else:
            i+=1
    return len(nums)
print(rd())