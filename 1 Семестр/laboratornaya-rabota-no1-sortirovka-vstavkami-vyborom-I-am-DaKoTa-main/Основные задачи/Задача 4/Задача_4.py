def Linear_sort(a, v):
    k=0
    for i in range (len(a)):
        if a[i] == v:
            k+=1
            indx.append(i)
    if len(indx)!=0:
        res = ' '.join(map(str, indx))
        return str(k) + "\n" + str(res)


with open('input.txt','r') as f:
    a = list(map(int, f.readline().split()))
    v = f.readline()
indx=[]
if (1 <= len(a) <= 10**3):
    if v!="":
        with open('output.txt', 'w') as f:
            f.write(str(Linear_sort(a,int(v))))
    else:
        with open('output.txt', 'w') as f:
            f.write(str(0) + "\n" + str(-1))