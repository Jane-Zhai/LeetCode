class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
        给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
        """
        sum_ = -num
        for i in range(1,int(num**0.5)+1):
            if num % i == 0:
                sum_ += i
                sum_ += num / i
        if sum_ == num:
            return True
        else:
            return False


sol = Solution()
print(sol.checkPerfectNumber(25))

# class Solution {
#     public boolean checkPerfectNumber(int num) {
#         switch(num) {
#             case 6:
#             case 28:
#             case 496:
#             case 8128:
#             case 33550336:
#                 return true;
#         }
#         return false;
#     }
# }