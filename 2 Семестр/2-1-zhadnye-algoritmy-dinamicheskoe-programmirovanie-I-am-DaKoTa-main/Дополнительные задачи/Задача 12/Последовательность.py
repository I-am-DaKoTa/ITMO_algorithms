with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))
    A.sort(reverse=True)
    s = sum(A)
    p, q = [], []
if s % 2 != 0 or n == 1:
    with open("output.txt", "w") as f:
        f.write("-1")
    exit()
else:
    for a in A:
        if sum(p) + a <= s // 2:
            p.append(a)
        else:
            q.append(a)
if sum(p) == sum(q):
    if len(p) <= len(q):
        with open("output.txt", "w") as f:
            f.write(str(len(p)) + '\n')
            for number in p:
                f.write(str(number) + ' ')
    else:
        with open("output.txt", "w") as f:
            f.write(str(len(q)) + '\n')
            for number in q:
                f.write(str(number) + ' ')
else:
    with open("output.txt", "w") as f:
        f.write("-1")
