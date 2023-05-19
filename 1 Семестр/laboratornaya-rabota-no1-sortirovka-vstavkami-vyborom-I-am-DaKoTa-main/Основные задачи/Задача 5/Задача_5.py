def selection_sort(a):
    for i in range(len(a) - 1):
        m = i
        j = i + 1
        while j < len(a):
            if a[j] < a[m]:
                m = j
            j += 1
        a[i], a[m] = a[m], a[i]
    return a

with open('input.txt','r') as f:
    a = list(map(int, f.readline().split()))
if 1 <= len(a) <= 10**3:
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, selection_sort(a))))
