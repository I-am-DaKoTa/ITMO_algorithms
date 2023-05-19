with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество объявдений
    a = list(map(int, f.readline().strip().split()))  # Прибыль за клик по i-му объявлению
    b = list(map(int, f.readline().strip().split()))  # Среднее количество кликов в день i-го слота
    a.sort(reverse=True)
    b.sort(reverse=True)
    result = 0
for i in range(n):
    result += a[i] * b[i]
with open('output.txt', 'w') as f:
    f.write(str(result))
