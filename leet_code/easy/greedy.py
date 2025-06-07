def min_coins(coins, amount):
    # Create DP array filled with infinity
    dp = [float('inf')] * (amount + 1)
    print(dp[0])
    dp[0] = 0  # Base case: 0 coins to make 0

    # Bottom-up DP
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [186, 419, 83, 408]
amount = 6249
print(min_coins(coins, amount))  # Expected: 20
