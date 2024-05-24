def backTrack(p,T):
    for i in range(0,len(T)-len(p)+1):
        if p[0] == T[i]:
            if p==T[i:i+len(p)]:
                return i
    return -1
#--------------------------------------------------#
def lastOccurrence(p,T):# Hàm tìm vị trí của các phần tử của T trong p nếu có nhiều vị trí thì lấy ở cuối
    x = list(set(T))# lấy những phần tử khác nhau trong T
    x.sort() 
    f = [] # mảng chứa vị trí nếu x[i] mà có trong p thì f[i] chứa vị trí của x[i] còn ko thì f[i]=-1
    for i in range(len(x)):#Duyệt các phần tử trong x
        vt=-1
        for j in range(len(p)-1,-1,-1): # Duyệt các phàn tử trong p
            if p[j]==x[i]: # Nếu tìm thấy x[i] trong p
                vt = j
                break
        f.append(vt)
    return x,f
 
def Boyer_Moore(p,T):
    x,f = lastOccurrence(p,T) # x: chứa chữ cái trong T, f chứa vị trí của những chữ cái đó trong p
    L = dict(zip(x,f))# gộp x và f thành dict có dạng {x[i]:f[i]}
    # phần dưới như trong slide
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
 
    

def failure(p): #Hàm tìm số chuỗi con bằng nhau trong tiền tố và hậu tố của chuỗi con p(p[0:i] với 0<i<len(p)) 
    f = [-1] # Xem trong slide để hiểu hàm f tính như nào
    for i in range(1,len(p)):# Duyệt độ dài chuỗi con của b
        count = 0
        for j in range(1,i): #duyệt các tiền tố và hậu tố trong chuỗi con
        	# Để hai chuỗi bằng nhau thì trước hết độ dài phải bằng nhau, nên ta chỉ xét những tiền tố và hậu tố cố độ dài bằng nhau trong chuỗi con
            if p[0:j] == p[i-j:i]: #Nếu tiền tố p[0:j] bằng hậu tố [i-j:i] (i-j vì để cho hai chuỗi nàu có độ dài bằng nhau và bằng j) 
                count = j
        f.append(count)
    return f
 
 
 
def Knuth_Morris_Pratt(p,T):
    f = failure(p)
    i=0
    j=0
    #Thuật toán bước nhảy như trong slide
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
 
