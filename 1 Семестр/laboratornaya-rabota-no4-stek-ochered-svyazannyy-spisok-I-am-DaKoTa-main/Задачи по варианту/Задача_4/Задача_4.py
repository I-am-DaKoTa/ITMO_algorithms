def correct_brackets(A):
    k = 1
    for x in A:
        if (x == "(") or (x == "[") or (x == "{"):
            stack.append(x)
            num_stack.append(str(k))
        elif (x == ")") or (x == "]") or (x == "}"):
            try:
                if not abs(ord(stack.pop()) - ord(x)) <= 2:
                    return str(k)
            except IndexError:
                return str(k)
            num_stack.pop()

        k += 1
    if not num_stack:
        return "Success"
    else:
        return ' '.join(num_stack)


with open('input.txt', 'r') as f:
    A = f.readline()
    stack = []
    num_stack = []
    if 1 <= len(A) <= 10 ** 5:
        with open('output.txt', 'w') as f:
            f.write(correct_brackets(A))
