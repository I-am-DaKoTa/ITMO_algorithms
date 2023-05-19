# Last In - First Out
with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.read().splitlines()
    stack = []


def create_stack(commands, n):
    for i in range(n):
        if len(stack) > 10 ** 6:
            return "Error"
        if "+" in commands[i]:
            if int(commands[i][2:]) > 10 ** 9:
                return "Error"
            stack.append(commands[i][2:])
        else:
            with open('output.txt', 'a') as f:
                f.write(stack.pop() + '\n')


if 1 <= n <= (10 ** 9):
    create_stack(commands, n)
