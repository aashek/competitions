def minAmount(coins, amount):
    dp = (amount + 1) * [100]
    for i in coins:
        dp[i] = 1

    dp[0] = 0

    for i in range(1, amount + 1):

        candidates = [dp[i - x] for x in coins if i >= x]
        dp[i] = min(1 + min(candidates), dp[i])
        # for j in coins:
        #     if j > i: continue
        #     dp[i] = min(dp[i], 1 + dp[i - j])

    print(dp)
    return dp[amount]


coins = [1, 2, 5]
amount = 10
print(minAmount(coins, amount))
