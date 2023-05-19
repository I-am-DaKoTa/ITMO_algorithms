import random

def Partition3(A, l, r):
    # Опорный элемент
    x = A[l]
    m1, m2 = l, l

    while m2 <= r:

        if A[m2] < x:
            (A[m2], A[m1]) = (A[m1], A[m2])
            m1 += 1
            m2 += 1

        elif A[m2] > x:
            (A[m2], A[r]) = (A[r], A[m2])
            r-=1
        else:
            m2+=1

    return (m1,m2)

# Функция для нахождения опорного элемента и разделения массива на три части
def Randomized_QuickSort3(A, l, r):
    if l < r:
        k = random.randint(l,r)
        A[l], A[k] = A[k], A[l]
        (m1,m2) = Partition3(A,l,r)
        Randomized_QuickSort3(A, l, m1-1)
        Randomized_QuickSort3(A, m2, r)
    return A

with open('input-2.txt','r') as f:
	n = int(f.readline())
	A = [int(x) for x in f.readline().split(' ')]
if 1 <= n <= (10**4) and not(any([abs(x)>10**9 for x in A])):
	with open('output-2.txt','w') as f:
		f.write(' '.join(map(str,Randomized_QuickSort3(A, 0, n - 1))))
