with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество целых чисел
    a = list(map(str, f.readline().strip().split()))  # Числа
    a.sort(key=lambda x: x * 5, reverse=True)

with open('output.txt', 'w') as f:
    f.write(''.join(map(str, a)))
