# Находим минимальную цену, если заказываем более крупную партию
def Big_Batch(N, A1, A2, A3, A4, A5, A6, A7):
    cost = 2 * 10 ** 10
    if 100000 < N <= 1000000:
        cost = A7
    elif 10000 < N <= 100000:
        cost = min(A6, A7)
    elif 1000 < N <= 10000:
        cost = min(A5, A6, A7)
    elif 100 < N <= 1000:
        cost = min(A4, A5, A6, A7)
    elif 10 < N <= 100:
        cost = min(A3, A4, A5, A6, A7)
    elif 1 < N <= 10:
        cost = min(A2, A3, A4, A5, A6, A7)
    return cost


# Находим минимальную цену, если заказываем с помощью комбинирования тарифов
def Combination(N, A1, A2, A3, A4, A5, A6, A7):
    cost = 0
    if N <= 9:
        cost = N * A1
    elif N <= 99:
        cost = ((N // 10) * A2) + ((N % 10) * A1)
    elif N <= 999:
        cost = ((N // 100) * A3) + (((N % 100) // 10) * A2) + ((N % 10) * A1)
    elif N <= 9999:
        cost = ((N // 1000) * A4) + (((N % 1000) // 100) * A3) + (((N % 100) // 10) * A2) + ((N % 10) * A1)
    elif N <= 99999:
        cost = ((N // 10000) * A5) + (((N % 10000) // 1000) * A4) + (((N % 1000) // 100) * A3) + (
                ((N % 100) // 10) * A2) + ((N % 10) * A1)
    elif N <= 999999:
        cost = ((N // 100000) * A6) + (((N % 100000) // 10000) * A5) + (((N % 10000) // 1000) * A4) + (
                ((N % 1000) // 100) * A3) + (((N % 100) // 10) * A2) + ((N % 10) * A1)
    else:
        cost = ((N // 1000000) * A7) + (((N % 1000000) // 100000) * A6) + (((N % 100000) // 10000) * A5) + (
                ((N % 10000) // 1000) * A4) + (((N % 1000) // 100) * A3) + (((N % 100) // 10) * A2) + (
                       (N % 10) * A1)
    return cost


with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    A1 = int(f.readline().strip())
    A2 = int(f.readline().strip())
    A3 = int(f.readline().strip())
    A4 = int(f.readline().strip())
    A5 = int(f.readline().strip())
    A6 = int(f.readline().strip())
    A7 = int(f.readline().strip())

with open('output.txt', 'w') as f:
    f.write(str(min(Big_Batch(N, A1, A2, A3, A4, A5, A6, A7), Combination(N, A1, A2, A3, A4, A5, A6, A7))))
