def largest_sum(a,b,c):
    if a>b:
        if b>c:
            return a**2 + b**2
        else:
            return a**2 + c**2
    else:
        if a<c:
            return b**2 + c**2 
        else:
            return b**2 + a**2


