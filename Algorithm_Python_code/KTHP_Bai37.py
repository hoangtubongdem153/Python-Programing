def failure(p):
    f = [-1]
    for i in range(1,len(p)):
        count = 0
        for j in range(1,i):
            if p[0:j] == p[i-j:i]:
                count = j
        f.append(count)
    return f

                

def Knuth_Morris_Pratt(p,T):
    f = failure(p)
    i=0
    j=0
    while(i<=(len(T)-len(p))):
        while (j<len(p)) and (p[j]==T[i+j]):
            j+=1
        if j == len(p):
            return i
        else:
            i = i+j-f[j]
            if f[j]==-1: j=0
            else: j = f[j]
    return -1
s1=input('Nhập vào s1: ')
s2=input('Nhập vào s2: ')
res = Knuth_Morris_Pratt(s1,s2)
if res==-1: 
    print('Không tìm thấy s1 trong s2')
else:
    print('Tìm thấy s1 tại vị trí',res)
    