class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。在所有完整词中，最短的单词我们称之为最短完整词。
        单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
        我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
        牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。
        """
        
        licensePlate = list(filter(str.isalpha, licensePlate.lower()))
        res = list()
        short = 15
        for word in words:
            l = len(licensePlate)
            for a in word:
                if a in licensePlate:
                    l -= 1
            if l == 0 and len(word)<short:
                res = word
                short=len(word)
            
        return res     


sol = Solution()
print(sol.shortestCompletingWord(" 1s3 456",["looks", "pest", "stew", "show"]))             
        