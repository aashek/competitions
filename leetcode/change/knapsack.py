values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
maxWeight = 8

def maxKnapSack(values,weights,maxWeight):
    if maxWeight == 0 or len(weights) == 0: return 0


    # find the candidates for picking from weights
    # and use the max value

    # set them all to a minimum value
    dp = (maxWeight + 1) * [0]

    for i, v in enumerate(weights):
        dp[v] = values[i]

    print(dp)
    combin = [(values[_], weights[_]) for _ in range(len(weights))]
    # print(combin)



    for i in range(1, maxWeight + 1):
        for pair in combin:
            if pair[1] > i: continue
            dp[i] = max(dp[i], dp[i - pair[1]] + pair[0])

    print(dp) 
    return dp[-1]

print(maxKnapSack(values,weights,maxWeight))