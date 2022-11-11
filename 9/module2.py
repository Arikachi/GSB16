def para(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return a+b+c
    else:
        return "cant form triangle"

def max(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    else:
        return "cant form triangle"