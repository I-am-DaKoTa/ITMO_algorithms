import itertools

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество городов
    distances = []  # Длины между городами
    for _ in range(n):
        distances.append(list(map(int, f.readline().strip().split())))
min_distance = 10 ** (6 + n + 1)
min_path = 0

# Генерация путей
for path in itertools.permutations(range(n)):
    # Считаем расстояние между городами
    distance = 0
    for i in range(n - 1):
        distance += distances[path[i]][path[i + 1]]
        if distance > min_distance:
            break
    # Обновление минимальной дистанции и минимального пути
    if distance < min_distance:
        min_distance = distance
        min_path = path

with open('output.txt', 'w') as f:
    f.write(str(min_distance) + '\n')
    f.write(' '.join(str(x + 1) for x in min_path))
