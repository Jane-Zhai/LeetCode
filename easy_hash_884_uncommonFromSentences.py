class Solution:
    def uncommonFromSentences(self, A, B):
        """
        给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
        如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
        返回所有不常用单词的列表。
        您可以按任何顺序返回列表。
        """
        A = A.split(" ")
        B = B.split(" ")
        dic = dict()
        res = list()

        for word in A:
            dic[word] = dic.get(word,0)+1
        for word in B:
            dic[word] = dic.get(word,0)+1

        for key,value in dic.items():
            if value==1:
                res.append(key)

        return res


class Solution2:
    def uncommonFromSentences(self, A, B):
        s = A + ' ' + B
        s = s.split(' ')
        s_set = set(s)
        re = []
        for i in s_set:
            if s.count(i) == 1:
                re.append(i)
        return re


sol = Solution2()
print(sol.uncommonFromSentences("apple apple","banana")) 