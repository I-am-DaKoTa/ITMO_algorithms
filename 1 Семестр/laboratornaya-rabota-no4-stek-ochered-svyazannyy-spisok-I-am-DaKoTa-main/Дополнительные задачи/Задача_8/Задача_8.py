def command(cmd, num1, num2):
    if cmd == "*":
        return num1 * num2
    elif cmd == "+":
        return num1 + num2
    else:
        return num1 - num2


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [x for x in f.readline().split(' ')]
    stack = []
if 1 <= n <= 10 ** 6:
    for i in range(n):
        digit = a[i].isdigit()
        if digit:
            stack.append(int(a[i]))
        elif len(stack) >= 2:
            num2 = stack.pop()
            num1 = stack.pop()
            res = command(a[i], num1, num2)
            stack.append(res)
        else:
            with open('output.txt', 'w') as f:
                f.write("Error")
if len(stack) == 1:
    with open('output.txt', 'w') as f:
        f.write(str(stack.pop()))
else:
    with open('output.txt', 'w') as f:
        f.write("Error")
