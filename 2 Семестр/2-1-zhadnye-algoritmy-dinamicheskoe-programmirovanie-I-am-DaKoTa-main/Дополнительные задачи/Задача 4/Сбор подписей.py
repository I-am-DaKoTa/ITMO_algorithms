def takeSecond(elem):
    return elem[1]


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество отрезков n
    segments = []  # Список для хранения отрезков
    for _ in range(n):
        a, b = map(int, f.readline().split())
        segments.append((a, b))

segments.sort(key=takeSecond)  # Сортировка по второму элементу

points = []  # список точек, которые будем использовать для покрытия отрезков
current_point = segments[0][1]  # начинаем с конца первого отрезка
points.append(current_point)

# проходимся по оставшимся отрезкам
for i in range(1, n):
    # Если начало следующего отрезка больше текущей точки,
    # то добавляем его конец
    if segments[i][0] > current_point:
        current_point = segments[i][1]
        points.append(current_point)

with open('output.txt', 'w') as f:
    f.write(str(len(points)) + '\n')
    for point in points:
        f.write(str(point) + ' ')
