def Quick_Sort(left, right):
    key = a[(left + right) // 2][0]
    i = left
    j = right
    while True:
        while a[i][0] < key:
            i += 1
        while a[j][0] > key:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        if i > j:
            break
    if left < j:
        Quick_Sort(left, j)
    if i < right:
        Quick_Sort(i, right)


def ver(m):
    if m == 1:
        return "ДА"
    for i in range(n):
        k = 0
        j = 0
        while j < len(A[a[i][0]]):
            if abs(i - A[a[i][0]][j]) % m == 0:
                k += 1
                A[a[i][0]].pop(j)

            j += 1
        if k == 0:
            return "НЕТ"

    return "ДА"

with open('input.txt', 'r') as f:
    n, m = list(map(int, f.readline().strip().split()))
    a = [int(x) for x in f.readline().split(' ')]
    A = {}
for i in range(n):
    a[i] = [int(a[i]), i]
    A[a[i][0]] = A.get(a[i][0], [])
    A[a[i][0]].append(a[i][1])
Quick_Sort(0, len(a) - 1)
with open('output.txt', 'w') as f:
    f.write(ver(m))
