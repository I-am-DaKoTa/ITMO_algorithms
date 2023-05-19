def takeSecond(elem):
    return elem[1]


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество лекций
    time = []  # Список начала и конца лекций
    for i in range(n):
        time.append(list(map(int, f.readline().strip().split())))
    time.sort(key=takeSecond)  # Сортировка по второму элементу

last_finish = 0
count = 0

for start, finish in time:
    # Если начало лекции не накладывается на конец другой, то
    # добавляем лекцию к общему количеству и
    # обновляем конечное время последней лекции
    if start >= last_finish:
        count += 1
        last_finish = finish

with open('output.txt', 'w') as f:
    f.write(str(count))
