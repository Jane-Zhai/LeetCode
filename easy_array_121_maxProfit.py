class Solution(object):
    def maxProfit(self, price):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.
        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        Note that you cannot sell a stock before you buy one

        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
        注意你不能在买入股票前卖出股票
        """
        pro = 0
        for buy in range(0,len(price)-1):
            for sell in range(buy+1,len(price)):
                pro = max(pro, price[sell]-price[buy])
        return(pro)


class Solution2:
    """
    动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
    """
    def maxProfit(self, prices):
        res = 0   # 最大收益
        minprice = prices[0]   # i位置之前的最小值
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minprice)     # 当前最大收益，等于之前最大收益，与当前值与之前最小值之差两个值的最大值 
            minprice = min(minprice, prices[i])
        return res


class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curSum=maxSum=0
        for i in range(1,len(prices)):
            curSum=max(0,curSum+prices[i]-prices[i-1])
            maxSum = max(curSum,maxSum)
        return maxSum


sol = Solution3()
print(sol.maxProfit([7,1,5,3,6,4]))