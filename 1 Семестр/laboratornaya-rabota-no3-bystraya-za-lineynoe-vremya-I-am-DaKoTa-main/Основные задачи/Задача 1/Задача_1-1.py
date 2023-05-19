import sys

sys.setrecursionlimit(1500)
import random


def Partition(A, l, r):
    # Опорный элемент
    x = A[l]
    m = l

    for i in range(l + 1, r + 1):
        if A[i] <= x:
            m += 1
            (A[m], A[i]) = (A[i], A[m])

    # Постановка опорного элемента на своё финальное положение
    (A[l], A[m]) = (A[m], A[l])

    # Вывод точки, где выполнено разделение
    return m


# Функция для нахождения опорного элемента и разделения массива на две части
def Partition_QuickSort(A, l, r):
    if l < r:
        # Нахождение опорной точки
        m = Partition(A, l, r)
        # Рекурсивный вызов функции слева от опорной точки
        Partition_QuickSort(A, l, m - 1)
        # Рекурсивный вызов функции справа от опорной точки
        Partition_QuickSort(A, m + 1, r)
    return A


def Randomized_QuickSort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        # Нахождение опорной точки
        m = Partition(A, l, r)
        # Рекурсивный вызов функции слева от опорной точки
        Randomized_QuickSort(A, l, m - 1)
        # Рекурсивный вызов функции справа от опорной точки
        Randomized_QuickSort(A, m + 1, l)
    return A


with open('input-1.txt', 'r') as f:
    n = int(f.readline())
    A = [int(x) for x in f.readline().split(' ')]
if 1 <= n <= (10 ** 4) and not (any([abs(x) > 10 ** 9 for x in A])):
    with open('output-1.1.txt', 'w') as f:
        f.write(' '.join(map(str, Partition_QuickSort(A, 0, n - 1))))
if 1 <= n <= (10 ** 4) and not (any([abs(x) > 10 ** 9 for x in A])):
    with open('output-1.2.txt', 'w') as f:
        f.write(' '.join(map(str, Randomized_QuickSort(A, 0, n - 1))))
