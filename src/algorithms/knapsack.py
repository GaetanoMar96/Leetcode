def knapsack(n: int, weights: list[int], values: list[int], W: int) -> int:
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] < j: #curr weight < curr capacity
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][W]