'''
Натуральное число N является числом Фибоначчи тогда и только тогда,
когда 5N^2 + 4 или 5N^2 - 4 является квадратом.
Квадратное число — число, являющееся квадратом некоторого целого числа
'''
import time
import os
import psutil

import math
t_start = time.perf_counter()
with open('input.txt', 'r') as f:
    n = int(f.readline())
    nums = f.read().splitlines()
for num in nums:
    if math.sqrt(5 * (int(num) ** 2) - 4) % 1 == 0 or math.sqrt(5 * (int(num) ** 2) + 4) % 1 == 0:
        with open('output.txt', 'a') as f:
            f.write("Yes" + '\n')
    else:
        with open('output.txt', 'a') as f:
            f.write("No" + '\n')
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
memoryUse = (psutil.Process(os.getpid()).memory_info()[0] / 2 ** 20)
print('Память:', memoryUse, 'мегабайт')