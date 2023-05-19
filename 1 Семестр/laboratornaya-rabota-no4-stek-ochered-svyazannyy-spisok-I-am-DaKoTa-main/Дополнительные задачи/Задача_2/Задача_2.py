# First In - First Out
with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.read().splitlines()
    queue = []


def create_queue(commands, n):
    for i in range(n):
        if len(queue) > 10 ** 6:
            return "Error"
        if "+" in commands[i]:
            if int(commands[i][2:]) > 10 ** 9:
                return "Error"
            queue.append(commands[i][2:])
        else:
            with open('output.txt', 'a') as f:
                f.write(queue.pop(0) + '\n')


if 1 <= n <= (10 ** 9):
    create_queue(commands, n)
