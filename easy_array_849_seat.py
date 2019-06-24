class Solution:
    def maxDistToClosest(self, seats):
        """
        在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
        至少有一个空座位，且至少有一人坐在座位上。
        亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
        返回他到离他最近的人的最大距离。
        """
        count = 0
        distance = 0
        for i,seat in enumerate(seats):
            if seat == 0:
                count += 1
            else:  # 直到第一个不是0的数的时候，算距离
                if i == count:  # 如果第一个座位到这里都是0
                    distance = count
                else:
                    if (count % 2) == 0:
                        distance = max(distance, count/2)
                    else:
                        distance = max(distance, (count+1)/2)
                count = 0

        return int(max(distance, count))

class Solution2:
    def maxDistToClosest(self, seats):

        distance, zero = 0, 0
        for index, seat in enumerate(seats):
            if seat == 0:
                zero += 1
            else:
                # 开始就为零的情况
                if index - zero == 0:
                    distance = zero
                else:
                    # 中间为零的情况， 奇数跟偶数不同
                    distance = max(distance, zero // 2 + 1 if zero & 1 else zero // 2)                
                zero = 0

        # 别忘记最后为零的情况        
        return max(zero, distance)

    
sol=Solution()
print(sol.maxDistToClosest([0,0,0,0,1,0,1]))
        