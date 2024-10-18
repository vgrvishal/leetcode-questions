if x<0:
    return False
    l=[]
    while x>0:
            rem=x%10
            l.append(rem)
            x=x//10
    i=0
    j=len(l)-1
    while(i<=j):
        if(l[i]==l[j]):
            i+=1
            j-=1
        else:
            return False
    return True