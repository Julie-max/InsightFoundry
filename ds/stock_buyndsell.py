class Solution:
    # Function to calculate maximum profit using single pass
    def stockbuySell(self, prices):
        buy=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy = prices[i]
            if prices[i]-buy>max_profit:
                max_profit = prices[i]-buy
        return max_profit

# Driver code
obj = Solution()
prices = [7,6,4,3,1]
print(obj.stockbuySell(prices))