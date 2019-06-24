# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def tree2list(root):
            if root:
                return [root.val,tree2list(root.left),tree2list(root.right)]
            return str(tree2list(t)) in str(tree2list(s))

class Solution2():
    def isSubtree(self,s,t):
        if not s:
            return False
        return self.subFrom(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def subFrom(self,s,t):
        if (not s and not t):   return True
        if (not s or not t):    return False
        if (s.val != t.val):    return False
        return self.subFrom(s.left, t.left) and self.subFrom(s.right, t.right)
