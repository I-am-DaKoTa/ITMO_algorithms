def insert(num, i):
    queue.append([num, i])


def delete():
    try:
        min_val = 0
        for i in range(len(queue)):
            if queue[i][0] < queue[min_val][0]:
                min_val = i
        item = queue[min_val][0]
        del queue[min_val]
        with open('output.txt', 'a') as f:
            f.write(str(item)+"\n")
    except IndexError:
        with open('output.txt', 'a') as f:
            f.write("*"+"\n")


def decrease_key(x, y):
    num = 0
    while x != queue[num][1]:
        num += 1
    queue[num] = [y, x]


with open('input.txt', 'r') as f:
    n = int(f.readline())
    queue = []
    if 1 <= n <= 10**6:
        for i in range(n):
            a = [x for x in f.readline().strip().split(' ')]
            if a[0] == "A":
                if abs(int(a[1]))<=10**9:
                    insert(int(a[1]), i + 1)
                else:
                    with open('output.txt', 'w') as f:
                        f.write("ERROR")
            elif a[0] == "X":
                delete()
            else:
                decrease_key(int(a[1]), int(a[2]))
    else:
        with open('output.txt', 'w') as f:
            f.write("ERROR")
