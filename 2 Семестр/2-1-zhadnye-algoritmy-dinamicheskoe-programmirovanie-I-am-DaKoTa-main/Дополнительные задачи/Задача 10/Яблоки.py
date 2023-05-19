with open('input.txt', 'r') as f:
    n, s = map(int, f.readline().split())  # Количество яблок и рост Алисы
    apples = []  # Список с яблоками и их свойствами
    for i in range(n):
        a, b = map(int, f.readline().split())
        apples.append((a, b, i + 1))
apples.sort(key=lambda x: (x[0], -x[1]))  # Сортируем яблоки по эффекту уменьшения и увеличивания

order = []
for a, b, i in apples:
    # Проверяем сможет ли Алиса съесть яблоко при этом,
    # чтобы её рост не стал меньше или равен нулю
    if s <= a:
        with open('output.txt', 'w') as f:
            f.write('-1')
        exit()
    s += (b - a)  # Добавляем разницу эффекта уменьшения и увеличения
    order.append(str(i))
with open('output.txt', 'w') as f:
    f.write(' '.join(order))