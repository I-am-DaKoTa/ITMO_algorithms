with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    result = 0
dp = [[0 for j in range(n + 1)] for i in range(10)]
for i in range(10):
    dp[i][1] = 1
for j in range(2, n + 1):
    for i in range(10):
        if i == 0:
            dp[0][j] = (dp[4][j - 1] + dp[6][j - 1])
        elif i == 1:
            dp[1][j] = (dp[6][j - 1] + dp[8][j - 1])
        elif i == 2:
            dp[2][j] = (dp[7][j - 1] + dp[9][j - 1])
        elif i == 3:
            dp[3][j] = (dp[4][j - 1] + dp[8][j - 1])
        elif i == 4:
            dp[4][j] = (dp[0][j - 1] + dp[3][j - 1] + dp[9][j - 1])
        elif i == 6:
            dp[6][j] = (dp[0][j - 1] + dp[1][j - 1] + dp[7][j - 1])
        elif i == 7:
            dp[7][j] = (dp[2][j - 1] + dp[6][j - 1])
        elif i == 8:
            dp[8][j] = (dp[1][j - 1] + dp[3][j - 1])
        elif i == 9:
            dp[9][j] = (dp[2][j - 1] + dp[4][j - 1])

for i in range(1, 10):
    if i != 8:
        result += dp[i][n]
with open("output.txt", "w") as f:
    f.write(str(result))
