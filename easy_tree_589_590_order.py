"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        递归
        :type root: Node
        :rtype: List[int]
        """
        def order(root,orderlist):
            if root is None:
                return None
            orderlist.append(root.val)
            for i in root.children:
                order(i,orderlist)
        
        orderlist = []
        order(root,orderlist)
        return orderlist

    def preorder2(self,root):
        # 迭代
        if root is None:
            return None
        res = []
        stack = [root]
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            temp = []
            for i in cur.children:
                temp.append(i)
            if len(temp):
                temp.reverse()
                stack.extend(temp)
        return res

class Solution2(object):
    def postorder(self, root):
        """
        递归
        :type root: Node
        :rtype: List[int]
        """
        def order(root,temp):
            if root is None:
                return None
            for i in root.children:
                order(i, temp)
                temp.append(i.val)
                
        
        temp = []
        order(root,temp)
        temp.append(root.val)
        return temp

    def postorder2(self, root):
        # 迭代
        if root is None:
            return None
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.insert(0,cur.val)
            if len(cur.children)>0:
                for i in cur.children:
                    stack.append(i)
        return res
