class Solution:
    def minCostClimbingStairs(self, cost):
        """"
        数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
        每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
        您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
        """
        count = 0
        i=1
        cost.insert(0,0)
        cost.append(0)
        while i<len(cost)-2:
            if cost[i] + cost[i+2] < cost[i+1]:
                count += cost[i]
                i += 1
            else:
                count += cost[i+1]
                i += 2
        return count

class Solution2:
    def minCostClimbingStairs(self, cost):
        """
        到达当前台阶时判断下从前一个台阶过来，还是从前一个的前一个过来，一直累加到最后一个台阶完，最小值就是最省体力的。
        """
        p1,p2 = 0, 0
        for i in range(2, len(cost)+1):
                    p1,p2 =p2, min(p2 + cost[i-1], p1 + cost[i-2])
        return p2

class Solution3:
    def minCostClimbingStairs(self, cost):
        # 动态规划， 唯一需要注意的是起点值为0， 
        # 终点的值不是数组的最后一位，而是0，即cost.append(0)
        last = 0
        now = 0
        cost.append(0)
        for val in cost:
            now, last = min(now+val,last+val), now
        return now

sol=Solution3()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))