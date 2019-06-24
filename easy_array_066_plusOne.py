class Solution1(object):
    def plusOne(self, digits):
        """
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.

        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
        最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头。
        """


        if digits.count(9) == len(digits):
            digits.insert(0,1)
            for i in range(1,len(digits)):
                digits[i] = 0
        else:
            for num in digits[::-1]:
                if num == 9:                
                    if digits[digits.index(num)-1] == 9:
                        continue
                    else:
                        digits[digits.index(num)] = 0
                else:
                    digits[digits.index(num)] += 1
                    break

        return digits


class Solution2:
    def plusOne(self, digits):
        for index in range(len(digits)-1,-1,-1):
            if digits[index] + 1 <10:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
                if index == 0:
                    digits.insert(0,1)
                    return digits


class Solution3(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in digits:
            sum = sum * 10 + i
        return [int(x) for x in str(sum+1)]


sol = Solution3()
print(sol.plusOne([9,9]))