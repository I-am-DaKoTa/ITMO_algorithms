import time
t_start = time.perf_counter()
import tracemalloc
with open('input.txt', 'r') as f:
    n, m = list(map(int, f.readline().strip().split()))
    a = [int(x) for x in f.readline().split(' ')]
    if (1 <= n <= 10 ** 5) and (0 <= m <= 10 ** 9) and (all([1 <= i <= 10 ** 6 for i in a])):
        x = m
        k = 1
        while x != 0:
            # Пока справок хватает на всю очередь и ни у кого не будет
            # отрицательного количества справок после раздачи
            while (x - (len(a)) >= 0) and (all([i > 0 for i in a])):

                while x - ((k+1) * len(a)) >= 0:
                    k+=1
                x -= len(a)*k
                a = [x - k for x in a]
                while a.count(0) != 0:
                    a.remove(0)
            if a[0] - 1 == 0 and x > 0:
                a.pop(0)
                x -= 1
            elif a[0] - 1 != 0 and x > 0:
                a[0]-=1
                a.append(a.pop(0))
                x -= 1
    if len(a) == 0:
        with open('output.txt', 'w') as f:
            f.write("-1")
    else:
        with open('output.txt', 'w') as f:
            f.write(str(len(a)))
            f.write("\n")
            f.write(' '.join(map(str, a)))
print("Время: %s секунд " % (time.perf_counter() - t_start))
print(tracemalloc.get_tracemalloc_memory())
tracemalloc.stop()
