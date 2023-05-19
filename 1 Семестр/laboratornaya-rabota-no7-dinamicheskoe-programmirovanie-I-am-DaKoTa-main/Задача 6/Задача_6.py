with open("input.txt", "r") as f:
    n = int(f.readline())
    A = [int(x) for x in f.readline().split()]

dp = [1] * n
lis = [[x] for x in A]

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            lis[i] = lis[j] + [A[i]]

max_length = max(dp)
index = dp.index(max_length)

with open("output.txt", "w") as output_file:
    output_file.write(str(max_length) + "\n")
    output_file.write(" ".join(map(str, lis[index])))