with open('input.txt', 'r') as f:
    d = int(f.readline().strip())  # Расстояние между городами в км
    m = int(f.readline().strip())  # Сколько может проехать км автомобиль на полном баке
    n = int(f.readline().strip())  # Количество заправок на пути
    stops = list(map(int, f.readline().strip().split()))  # Остановки

last_stop = 0  # Последняя остановка
count = 0  # Количество дозаправок
remaining_distance = d  # Сколько нам осталось проехать

# Проверяем нужно ли нам вообще заправляться
# Если можем проехать без дозаправок, то выводим 0
if d <= m:
    with open('output.txt', 'w') as f:
        f.write('0')
    exit()

for i in range(n):
    distance_to_next_stop = stops[i] - last_stop  # Расстояние до следующей заправки

    # Проверяем сможем ли вы проехать до следующей заправки на полном баке
    # Если нет, то выводим -1
    if distance_to_next_stop > m:
        with open('output.txt', 'w') as f:
            f.write('-1')
        exit()

    # Проверяем сможем ли мы проехать до следующей заправки без дозаправки
    # Если нет, то заправляемся
    elif distance_to_next_stop > remaining_distance - m:
        last_stop = stops[i]
        count += 1
        remaining_distance = d - last_stop

    # Спокойно едем дальше
    else:
        remaining_distance -= distance_to_next_stop

with open('output.txt', 'w') as f:
    f.write(str(count))
