class Solution:
    def findRestaurant(self, list1, list2):
        """
        假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
        你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
        """
        index = len(list1) + len(list2)
        res = list()
        for rest in list1:
            if rest in list2:
                if index >= (list1.index(rest) + list2.index(rest)):
                    res.append(rest)
                    index = list1.index(rest) + list2.index(rest)
                     
            if list1.index(rest) > index:
                break

        return res


sol = Solution()
print(sol.findRestaurant(["Shogun", "KFC", "Burger King"],["KFC", "Shogun", "Burger King"]))