# Set Min[i] equal to Infinity
# for all of i
# Min[0] = 0

# For i = 1 to S
# For j = 0 to N - 1
# If(Vj <= i AND Min[i - Vj] + 1 < Min[i])
# Then Min[i] = Min[i - Vj] + 1

# Output Min[S]

coins = [1,3,5]
S = 11 # Number

def minCoins(coins,S):
    dp = [1e9] * (S + 1)
    dp[0] = 0

    # for i in coins:
    #     dp[i] = 1

    # algo for
    # for all subproblems (numbers less than 11)

        # loop through the coins we have

            # if curr amount > curr coin value:
                # check if the value minusing the coin is less than curr no of coins.


    for i in range(1, S + 1):
        for j in coins:
            if j <= i and dp[i - j] + 1 < dp[i]:
                dp[i] = dp[i - j] + 1

    print(dp)
    return dp[-1]
print(minCoins(coins,S))