with open('input.txt', 'r') as f:
    n = int(f.readline().strip())  # Количество конфет
k, s = 1, 0
numbers = []  # Призы
while n >= s + k:
    numbers.append(k)
    s += k
    k += 1
if n - s > 0:
    numbers[-1] += n - s
with open('output.txt', 'w') as f:
    f.write(str(len(numbers)) + '\n')
    for number in numbers:
        f.write(str(number) + ' ')
