def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j + 1], a[j]
    return a

with open('input.txt','r') as f:
    a = list(map(int, f.readline().split()))
if 1 <= len(a) <= 10**3:
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, bubble_sort(a))))
