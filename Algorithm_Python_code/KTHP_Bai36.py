def lastOccurrence(p,T):
    x = list(set(T))
    x.sort()
    f = []
    for i in range(len(x)):
        vt=-1
        for j in range(len(p)-1,-1,-1):
            if p[j]==x[i]: 
                vt = j
                break
        f.append(vt)
    return x,f
    
def Boyer_Moore(p,T):
    x,f = lastOccurrence(p,T)
    L = dict(zip(x,f))
    i = len(p)-1
    j = len(p)-1
    while(i<len(T)):
        while (j>=0) and (T[i]==p[j]): 
            i-=1
            j-=1
        if (j==-1): 
            return i+1
        else: 
            i = i+len(p)-min(j,1+L[T[i]])
            j = len(p)-1
    return -1
s1=input('Nhập vào s1: ')
s2=input('Nhập vào s2: ')
res = Boyer_Moore(s1,s2)
if res==-1: 
    print('Không tìm thấy s1 trong s2')
else:
    print('Tìm thấy s1 tại vị trí',res)
    
# Thuật toán BM hiệu quả trong chuỗi chứa tập kí tự lớn như bảng chữ cái lớn A..Z,a..z,1..9,..
# Không hiệu quả trong trường chứa tập kí tự nhỏ như nhị phân