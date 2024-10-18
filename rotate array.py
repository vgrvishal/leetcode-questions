def ra():
    k=int(input())
    nums=[1,2,3,4,5,6,7]

    k=k%len(nums)
    for i in range(k):
        
        p=nums.pop(-1)
        nums.insert(0,p)
    

    return nums
print(ra())