def gw():
    v = "A man, a plan, a canal: Panama"
    
    r=v.replace(" ","")
    
    v=''.join(filter(lambda x: x.isalnum() or x.isspace(), r))
    v=v.lower()
    
    a=v[::-1]
    
    return v==a
    
    
print(gw())