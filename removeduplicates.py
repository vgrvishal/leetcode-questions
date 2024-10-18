def rd():
    nums=[1,1,1,2,2,3]
    i=1
    while i < len(nums):
        if nums[i]==nums[i-1]:
            nums.pop(i)
        
        else:
            i+=1
    return nums
print(rd())