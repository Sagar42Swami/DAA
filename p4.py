def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # The last cell will have the maximum value
    return dp[n][capacity]


# Driver Code
if __name__ == "__main__":
    values = [50,200,280]
    weights = [10, 20, 30]
    capacity = 50

    print("0-1 Knapsack Problem using Dynamic Programming")
    max_value = knapsack_01(values, weights, capacity)
    print("Maximum value in Knapsack =", max_value)
