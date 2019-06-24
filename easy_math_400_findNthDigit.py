class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
        """
        if n < 10:
            return n
        # 1 - [1,9]             9
        # 2 - [10,99]          90
        # 3 - [100,999]       900
        # 4 - [1000,9999]    9000
        length = 0
        cnt = 9
        i = 1
        # 计算前缀部分，全部被占用部分总共有多少位即length。
        while length + cnt*i < n:
            length += cnt * i
            cnt *= 10
            i += 1
        # 计算尾部
        # 其一、计算第一个数字即pow(10, i-1)-1。
        # 其二、推理出最后一个出现的多位数字即num，并计算出位于第几位即index
        num = 10 ** (i-1) -1 +(n-length+1)//i
        index = (n-length-1)%i
        res = str(num)[index]
        return int(res)

sol = Solution()
print(sol.findNthDigit(1001))


# class Solution {
#      # 长度为1的数字，[1,9]共有9个数字，组成的字符串长度为9 * 长度1 == 9
#         # 长度为2的数字，[10,99]一共90个数字，组成的字符串长度为90 * 长度2 = 180
#         # 长度为3的数字，[100, 999]一共900个数字，组成的字符串长度为900 * 长度3 = 2700
#         # ...
#         # 长度为n的数字，[pow(10, len - 1),  pow(10, len)),一共 9 * pow(10, len - 1)个数，组成的字符串长度为 9 * pow(10, len - 1) * len
 
# public:
#     int findNthDigit(int n) {
#         if (n < 10){
#             return n;
#         }
#         int len = 0;//单个数字的长度
#         long long nextSize = pow(10, len) * (len + 1) * 9;//长度为len + 1的数字所构成的字符串的长度
#         //第一步：确定n所处的数字的位数
#         while (n > nextSize){
#             n -= nextSize;
#             len += 1;
#             nextSize = pow(10, len) * (len + 1) * 9;//长度为len + 1的数字所构成的字符串的长度
#         }
#         //第二步：确定n是出于位数为len + 1的数字中的第几个数字，并且转换为字符串
#         string resStr = to_string((long long)pow(10, len) + (n - 1) / (len + 1));
#         //返回n在这个数字中对应的位，（比如当n == 15，求得len = 1，n = 6， resStr = “12”,然后取出“12”字符串的第二位）
#         return resStr[n - (n - 1) / (len + 1) * (len + 1) - 1] - '0';//注意返回的int数字，并不是返回字符'k',需要减去'0'
#     }
# };
