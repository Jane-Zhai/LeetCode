class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = list()
        for i in range(12):
            for j in range(60):
                if self.count1(i) + self.count1(j) == num:
                    res = str(i) + ":"
                    if j > 9:
                        res += str(j) 
                    else:
                        res += "0"+str(j)
                    ret.append(res)
        return ret
    def count1(self,n):
        # 计算二进制中1 的个数
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res


sol = Solution()
print(sol.readBinaryWatch(1))


# 提几点改进意见

# hour最大为3，minute最大为5，num最大为8；
# hour>num时无效，应该及时跳过，但是比如num=1，当i=7时 hour=3>1,应该cotinue而非break，因为有效的i=8（hour=1)就在后头
# 总结：

# 不应用unordered_map
# 分为0-12，0-59解题化排列组合化为简单的两数之和为定值的问题
# 二进制表示为时分时，10个二进制位是占不满的，hour最多3位，minute最多5位
# class Solution {
# public:
#     vector<string> readBinaryWatch(int num) {
#         vector<string> v;
#         if(num<0 || num>8) return v;
#         for(int i=0;i<12;++i)
#         {
#             auto hour=count_ones(i);
#             auto minute=num-hour;
#             if(hour>num)
#                 continue;
#             for(int j=0;j<60;++j)
#             {
#                 if(minute==count_ones(j))
#                 {
#                     string s1(to_string(i));
#                     v.push_back(s1+":"+(j<10? "0"+to_string(j): to_string(j) ) );
#                 }
#             }
#         }
#         return v;   
#     }
#     private:
#         inline int count_ones(int i)
#         {
#             int cnt=0;
#             while(i>0)
#             {
#                 cnt+=(i&1);
#                 i>>=1;
#             }
#             return cnt;
#         }
# };