def min_heapify(a, n, i):
    global m
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] < a[smallest]:
        smallest = left

    if right < n and a[right] < a[smallest]:
        smallest = right

    if smallest != i:
        m += 1
        res.append([i, smallest])
        a[i], a[smallest] = a[smallest], a[i]

        min_heapify(a, n, smallest)


def min_heap(a, n):

    for i in range(int(n // 2) - 1, -1, -1):
        min_heapify(a, n, i)


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split(' ')]
    m = 0
    res = []

if (1 <= n <= 10 ** 5) and (any([(0 <= i <= 10 ** 9) for i in a])):
    min_heap(a, n)

with open('output.txt', 'a') as f:
    if 0 <= m <= 4*n:
        f.write(str(m)+'\n')
        for _ in range(m):
            f.write(' '.join(map(str, res[_])) + '\n')
    else:
        f.write("ERROR")

