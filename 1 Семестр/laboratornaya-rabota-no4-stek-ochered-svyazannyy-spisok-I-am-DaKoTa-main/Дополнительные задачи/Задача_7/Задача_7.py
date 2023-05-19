def get_max(num, stack, stack_max, m, i):
    if not stack:
        stack.append(num)
        stack_max.append(num)
    else:
        stack.append(num)
        while stack_max and stack_max[-1] < num:
            stack_max.pop()
        stack_max.append(num)
    if i >= (m-1):
        with open('output.txt', 'a') as f:
            f.write(str(stack_max[0])+' ')
        try:
            if stack[0] == stack_max[0]:
                stack.pop(0)
                stack_max.pop(0)
            else:
                stack.pop(0)
        except IndexError:
            with open('output.txt', 'w') as f:
                f.write("Error")


with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readline().split(' ')]
    m = int(f.readline())
    stack = []
    stack_max = []
    if (1 <= n <= 10**5) and (1 <= m <= n):
        for i in range(n):
            if 0 <= a[i] <= 10**5:
                get_max(a[i], stack, stack_max, m, i)
            else:
                with open('output.txt', 'w') as f:
                    f.write("Error")
    else:
        with open('output.txt', 'w') as f:
            f.write("Error")