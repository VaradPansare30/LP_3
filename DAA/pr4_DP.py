n = 3

weight = [2, 3, 4]
profit = [12, 20, 30]

W = 5

# Create DP table
dp = []

for i in range(n + 1):
    row = [0] * (W + 1)
    dp.append(row)

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, W + 1):

        if weight[i - 1] <= w:
            dp[i][w] = max(
                profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Print maximum profit
print("Maximum Profit:", dp[n][W])

# Find selected items
w = W

print("Selected Items:")

for i in range(n, 0, -1):

    if dp[i][w] != dp[i - 1][w]:
        print("Item", i)
        w = w - weight[i - 1]