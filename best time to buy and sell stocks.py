def maxProfit(prices):
    profit=0
    mini=prices[0]
    for i in range(1,len(prices)):
        cost=prices[i]-mini
        profit=max(cost,profit)
        mini=min(mini,prices[i])
    return profit

prices=[7,1,5,3,6,4]
print(maxProfit(prices))