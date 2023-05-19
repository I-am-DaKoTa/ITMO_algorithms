def push(num, stack, stack_min):
    if not stack:
        stack.append(num)
        stack_min.append(num)
    else:
        stack.append(num)
        while stack_min and stack_min[-1] > num:
            stack_min.pop()
        stack_min.append(num)


def pop(stack, stack_min):
    try:
        if stack[0] == stack_min[0]:
            stack.pop(0)
            stack_min.pop(0)
        else:
            stack.pop(0)
    except IndexError:
        with open('output.txt', 'w') as f:
            f.write("Error")


def get_min(stack_min):
    with open('output.txt', 'a') as f:
        f.write(str(stack_min[0]) + '\n')


with open('input.txt', 'r') as f:
    n = int(f.readline())
    stack = []
    stack_min = []
    commands = f.read().splitlines()
for i in range(n):
    cmd = commands[i].split()
    if cmd[0] == '+':
        if 0 <= int(cmd[1]) <= 10 ** 9:
            push(cmd[1], stack, stack_min)
        else:
            with open('output.txt', 'w') as f:
                f.write("Error")
                break
    elif cmd[0] == '-':
        pop(stack, stack_min)
    elif cmd[0] == '?':
        get_min(stack_min)
