import time
import os
import psutil


def get_depth(ords, ind):
    parent = ords[ind]
    if parent == -1:
        depth = 1
    else:
        depth = get_depth(ords, parent) + 1
    return depth


def max_depth(ords):
    m = get_depth(ords, 0)
    print('m:',m)
    print('ords:',ords)
    for ind, parent in enumerate(ords):
        print('ind,parent:',ind,parent)
        depth = get_depth(ords, ind)
        print('depth',depth)
        if m < depth:
            m = depth
    return m


t_start = time.perf_counter()
with open('input.txt', 'r') as f:
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split(' ')]

if (1 <= n <= 10 ** 5) and (any([0 <= x <= (n - 1) for x in arr])):
    with open('output.txt', 'w') as f:
        f.write(str(max_depth(arr)))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
memoryUse = (psutil.Process(os.getpid()).memory_info()[0] / 2 ** 20)
print('Память:', memoryUse, 'мегабайт')
