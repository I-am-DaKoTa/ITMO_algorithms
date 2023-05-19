with open('input.txt', 'r') as f:
    W, n = map(int, f.readline().split())  # Вместимость сумки и количество золотых слитков
    w = list(map(int, f.readline().strip().split()))  # Вес золотых слитков

dp = [[0] * (W+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, W+1):
        dp[i][j] = dp[i-1][j]  # Если i-й слиток не положили
        if j >= w[i-1]:  # Если i-й слиток положили
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + w[i-1])

with open("output.txt",'w') as f:
    f.write(str(dp[n][W]))
