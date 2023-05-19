def correct_brackets(A):
    while '()' in A or '[]' in A:
        A = A.replace('()', '')
        A = A.replace('[]', '')
    if A:
        return "NO"
    else:
        return "YES"

with open('input.txt', 'r') as f:
    n = int(f.readline())
    A = f.read().splitlines()
    if 1 <= n <= 500:
        for i in range(n):
            if 1 <= len(A[i]) <= 10**4:
                with open('output.txt', 'a') as f:
                    f.write(correct_brackets(A[i]) + '\n')
