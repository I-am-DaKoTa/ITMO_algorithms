with open('input.txt', 'r') as f:
    K, n = map(int, f.readline().split())  # Рабочий день K минут, n сапог
    t = list(map(int, f.readline().strip().split()))  # Количество минут, которые требуются,
    # чтобы починить i-й сапог.
    t.sort()
    boots = 0  # Количество сапог

for i in range(n):
    if K >= t[i]:
        K -= t[i]
        boots += 1
    else:
        break

with open('output.txt', 'w') as f:
    f.write(str(boots))
