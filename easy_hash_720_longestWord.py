class Solution:
    def longestWord(self, words):
        """
        给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
        若无答案，则返回空字符串。
        """
        words = sorted(words)
        
        for i in range(len(words)-1):
            if words[i+1][:-1] == words[i]:
                res = words[i+1]
        return res

sol = Solution()
print(sol.longestWord(["a", "banana", "app", "appl", "apply", "apple","w","wo","wor","worl", "world"])) 