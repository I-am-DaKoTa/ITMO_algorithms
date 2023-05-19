with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))
    A.sort(reverse=True)
    s = sum(A)
    x, y, z = [], [], []
if s % 3 != 0 or n <= 2:
    with open("output.txt", "w") as f:
        f.write("0")
    exit()
else:
    for a in A:
        if sum(x) + a <= s // 3:
            x.append(a)
        elif sum(y) + a <= s // 3:
            y.append(a)
        else:
            z.append(a)
if sum(x) == sum(y) == sum(z):
    with open("output.txt", "w") as f:
        f.write("1")
else:
    with open("output.txt", "w") as f:
        f.write("0")
