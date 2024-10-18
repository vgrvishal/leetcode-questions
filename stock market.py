def mp():
    prices=[7,1,5,3,6,4]
    max1=0
    
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]>prices[i]:
                m=prices[j]-prices[i]
                if m>max1:
                    max1=m
        
    return max1
print(mp())