def du():
    nums=[1,2,3,4]

    dict={}
    def update(dict,key):
        dict[key]=dict.get(key,0)+1
    for j in nums:
        update(dict,j)
    flag=True
    result=0
    for key,value in dict.items():
        if value == 1:
            
            flag = False
        else:
            flag = True
            break
    return flag
print(du())