def fi():
    arr = [1]
    l=[]
    a=l+arr
    a.sort()
    print(a)
    n=len(a)
    print(n)
    for i in range(n):
        if n<2:
            return a[i]
        elif n%2!=0:
            r=(n-1)//2
            m=a[r]
        elif n%2==0:
            r=n//2
            r1=(n-2)//2
            m=(a[r]+a[r1])/2
    return m
    
print(fi())