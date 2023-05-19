def push(num, stack):
    if stack:
        num_max = max(num, stack[-1][1])
    else:
        num_max = num
    stack.append((num, num_max))


with open('input.txt', 'r') as f:
    n = int(f.readline())
    stack = []
    commands = f.read().splitlines()
    if 1 <= n <= 400000:
        for i in range(n):
            cmd = commands[i].split()
            if cmd[0] == 'push':
                if 0 <= int(cmd[1]) <= 10 ** 5:
                    push(int(cmd[1]), stack)
                else:
                    with open('output.txt', 'w') as f:
                        f.write("Error")
                        break
            elif cmd[0] == 'pop':
                try:
                    stack.pop()
                except IndexError:
                    with open('output.txt', 'w') as f:
                        f.write("Error")
                        break
            elif cmd[0] == 'max':
                with open('output.txt', 'a') as f:
                    f.write(str(stack[-1][1])+'\n')