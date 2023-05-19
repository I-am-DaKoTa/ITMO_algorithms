def check(n, a):
    for i in range(1, n + 1):
        if 2 * i <= n:
            if not (a[i - 1] <= a[(2 * i) - 1]):
                return False
        if 2 * i + 1 <= n:
            if not (a[i - 1] <= a[2 * i]):
                return False
    return True


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split(' ')]

if check(n, a):
    with open('output.txt', 'w') as f:
        f.write("YES")

else:
    with open('output.txt', 'w') as f:
        f.write("NO")
