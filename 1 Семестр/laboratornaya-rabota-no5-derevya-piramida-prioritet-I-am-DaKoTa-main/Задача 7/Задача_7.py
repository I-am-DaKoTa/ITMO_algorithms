def heapify(a, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] < a[smallest]:
        smallest = left

    if right < n and a[right] < a[smallest]:
        smallest = right

    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]

        heapify(a, n, smallest)


def heapSort(a, n):
    for i in range(int(n // 2) - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, -1, -1):
        a[0], a[i] = a[i], a[0]

        heapify(a, i, 0)


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split(' ')]

with open('output.txt', 'w') as f:
    if (1 <= n <= 10 ** 5) and (any([(abs(i) <= 10 ** 9) for i in a])):
        heapSort(a, n)
        f.write(' '.join(map(str, a)))
    else:
        f.write("ERROR")
