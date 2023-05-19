import time
t_start = time.perf_counter()
def Partition3(A, l, r):
    x = A[l][0]
    m1, m2 = l, l
    while m2 <= r:
        if A[m2][0] < x:
            (A[m2], A[m1]) = (A[m1], A[m2])
            m1 += 1
            m2 += 1
        elif A[m2][0] > x:
            (A[m2], A[r]) = (A[r], A[m2])
            r-=1
        else:
            m2+=1
    return (m1,m2)

def Randomized_QuickSort3(A, l, r):
    if l < r:
        (m1,m2) = Partition3(A,l,r)
        Randomized_QuickSort3(A, l, m1-1)
        Randomized_QuickSort3(A, m2, r)
    return A

with open('input.txt','r') as f:
	# n - количество точек; k - количество точек к началу координат среди данных n точек.
	n,k = list(map(int, f.readline().strip().split()))
	coords = []
	result = []
	for i in range(n):
		coords.append([int(x) for x in f.readline().split()])
		coords[i].insert(0,((coords[i][0])**2 + (coords[i][1])**2)**0.5)

if (1 <= n <= 10**5) and not(any([abs(coords[x][1])>10**9 for x in range(len(coords))])) and not(any([abs(coords[y][2])>10**9 for y in range(len(coords))])):
    Randomized_QuickSort3(coords, 0, n - 1)
    for i in range(k):
        result.append(coords[i][1:])

    with open('output.txt', 'w') as f:
        f.write(','.join(map(str,result)))
print("Время: %s секунд " % (time.perf_counter() - t_start))