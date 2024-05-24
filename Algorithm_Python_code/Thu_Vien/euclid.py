def gcd(a,b):
    while b>0:
        tmp = a % b
        a = b
        b = tmp
    return a

def extendEuclid(a,b):
    (u,v) = (a,b)
    (x1,x2) = (0,1)
    (y1,y2) =(1,0)
    while v !=0:
        (q, r) = (int(u/v), u%v)
        (x, y) =  (x2 - q*x1, y2 - q*y1)
        (x1, x2, y1, y2) = (x, x1, y, y1)
        (u, v) = (v, r)
    return (u,x2,y2)


