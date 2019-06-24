from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time):
        """
        在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
        返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。
        """
        # count = 0
        # for i in range(len(time)):
        #     for j in range(i+1,len(time)):
        #         if (time[i]+time[j]) % 60 == 0:
        #             count += 1
        # return count

        # 主要是两个时间t1,t2要想能被60整除，
        # 就需要t2 % 60 = 60 - t1 % 60， 要处理下mod 60为0的情况。 
        # 遇到一个t，则看下map里是否存在map[t%60]，
        # 如果存在，那么可以和以往的组成n对（n为t%60的计数） 
        # 同时将60 - t % 60加入map，方便后续遍历到的t计算。
        ans = 0
        modm = defaultdict(int)
        for t in time:
            mod = t%60
            if mod == 0:
                rem = 0
            else:
                rem = 60-mod

            ans += modm[mod]
            modm[rem]+= 1

        return ans

sol = Solution()
print(sol.numPairsDivisibleBy60([30,20,150,100,40]))