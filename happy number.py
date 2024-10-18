def du():
    n=int(input("enter : "))
    s=set()
    s.add(n)
    
    
    while n!=1:
        n=sqr(n)
        if n in s:
            return False
        else:
            s.add(n)
    return True


def sqr(n):
    result=0
    while n!=0:
        rem=n%10
        result+=rem*rem
        n=n//10
    return result
    