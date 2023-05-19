def heapify(a, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] < a[smallest]:
        smallest = left

    if right < n and a[right] < a[smallest]:
        smallest = right

    if smallest != i:
        (a[i], a[smallest]) = (a[smallest], a[i])

        heapify(a, n, smallest)


def heapSort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, -1, -1):
        (a[0], a[i]) = (a[i], a[0])

        heapify(a, i, 0)


def h_index(a):
    h = 0
    n = len(a)
    for i in range(n):
        if a[i] >= (i + 1):
            h += 1
    return h


with open('input.txt', 'r') as f:
    a = [int(x) for x in f.readline().split(',')]
    heapSort(a)

with open('output.txt', 'w') as f:
    f.write(str(h_index(a)))
