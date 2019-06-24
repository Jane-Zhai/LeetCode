# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, num):
            if not node:
                return 0
            num = num*2 + node.val
            if not node.left and not node.right:
                return num
            
            return dfs(node.left,num) + dfs(node.right,num)
        
        return dfs(root,0)