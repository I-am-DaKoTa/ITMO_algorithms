def lcsOf3(A, B, C, n, m, l):
    array = [[[0 for _ in range(l + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(l + 1):
                if (i == 0 or j == 0 or k == 0):
                    array[i][j][k] = 0

                elif (A[i - 1] == B[j - 1] and
                      A[i - 1] == C[k - 1]):
                    array[i][j][k] = array[i - 1][j - 1][k - 1] + 1

                else:
                    array[i][j][k] = max(max(array[i - 1][j][k], array[i][j - 1][k]),array[i][j][k - 1])

    return array[n][m][l]


with open('input.txt', 'r') as f:
    n = int(f.readline())
    A = [int(x) for x in f.readline().split(' ')]
    m = int(f.readline())
    B = [int(x) for x in f.readline().split(' ')]
    l = int(f.readline())
    C = [int(x) for x in f.readline().split(' ')]

with open('output.txt', 'w') as f:
    f.write(str(lcsOf3(A, B, C, n, m, l)))
