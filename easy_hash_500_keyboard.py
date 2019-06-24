class Solution0:
    def findWords(self, words):
        """
        给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
        """

                    
class Solution:
    def findWords(self, words):
        a = 'qwertyuiop'
        b = 'asdfghjkl'
        c = 'zxcvbnm'
        res = []
        for str in words:
            small_str = str.lower()
            x = []
            for lit in small_str:
                if lit in a:
                    x.append('a')
                elif lit in b:
                    x.append('b')
                else:
                    x.append('c')
            if len(set(x)) == 1:
                res.append(str)
        return res

class Solution2(object):
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)        
        return res


sol = Solution3()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))
