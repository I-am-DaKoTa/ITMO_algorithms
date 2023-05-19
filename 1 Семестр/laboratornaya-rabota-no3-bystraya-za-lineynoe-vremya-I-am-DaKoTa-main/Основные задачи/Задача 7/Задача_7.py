def RadixSort(A,n,m,k,indx):
    new_k=0
    for i in range(n-1,-1,-1):
        if new_k==k:
            break
        for j in range(m-1):
            if A[i][j] > A[i][j + 1]:
                indx[j],indx[j+1]=indx[j+1],indx[j]
                for x in range(i+1):
                    A[x][j], A[x][j+1] = A[x][j+1], A[x][j]
        new_k+=1
    return A,indx

with open('input.txt', 'r') as f:
    # n - число строк; m - длина строк; k - число фаз цифровой сортировки
    n, m, k = list(map(int, f.readline().strip().split()))
    A = []
    indx=[]
    for i in range(n):
        A.append(list(f.readline().strip()))
        indx.append(i+1)

if (1 <= n <= 10**4) and (1 <= k <= m <= 10**6) and (n*m<=5*10**7):
	with open('output.txt','w') as f:
		f.write(' '.join(map(str,RadixSort(A, n, m, k,indx)[-1])))
