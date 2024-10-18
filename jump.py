while len(nums)<3:
        if len(nums)==2 and nums[0]==0:
                return False
        elif len(nums)==1 or len(nums)==2:
                return True

        # elif len(nums)<=2:
        #     return False--
        
        s=len(nums)
        k=2
        l=[]
        for i in range(k,s):
            l.append(nums[i])
        if nums[1]==len(l) or (nums[1]==0 and nums[2]==0):
            return True
        else:
            return False