with open('input.txt', 'r') as f:
    n, W = map(int, f.readline().split())  # n - количество предметов, W - вместимость сумки
    parameters = []  # цена за 1 единицу веса, вес, цена
    for _ in range(n):
        p, w = map(int, f.readline().split())
        parameters.append((p / w, w, p))
    parameters.sort(reverse=True)
    total_value = 0

for ratio, weight, price in parameters:
    # Если вместимость 0, то выводим ответ 0
    if W == 0:
        break
    # Если мы можем положить в рюкзак полностью предмет,
    # то мы так и делаем
    elif W >= weight:
        total_value += price
        W -= weight
    # Если мы не можем положить в рюкзак полностью предмет,
    # то делим его и помещаем в рюкзак дробную часть
    else:
        fraction = W / weight
        total_value += price * fraction
        W = W - (weight * fraction)

with open('output.txt', 'w') as f:
    f.write(str(round(total_value, 4)))
