class Solution:
    def isAlienSorted(self, words, order):
        """
        某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
        给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
        """
        if len(words) == 1:
            return True
        
        trans = str.maketrans(order, 'abcdefghijklmnopqrstuvwxyz')
        
        nw = [ w.translate(trans) for w in words]
        
        for i in range(len(words) - 1):
            if nw[i] > nw[i + 1]:
                return False
        
        return True


class Solution2:
    def isAlienSorted(self, words, order):
        word_dict = {value: index for index, value in enumerate(order)}

        def helper(word_a, word_b):
            for w_a, w_b in zip(word_a, word_b):
                if word_dict[w_a] < word_dict[w_b]:
                    return True
                elif word_dict[w_a] > word_dict[w_b]:
                    return False
            if len(word_a) > len(word_b):
                return False
            return True

        for i in range(len(words) - 1):
            if not helper(words[i], words[i + 1]):
                return False
        return True


sol = Solution()
print(sol.isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz")) 