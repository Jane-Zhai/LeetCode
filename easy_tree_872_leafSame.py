# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def leafSimilar(self, root1, root2):
        """
        请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf(root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                self.res.append(root.val)
                return self.res
            leaf(root.left)
            leaf(root.right)
        
        if leaf(root1) == leaf(root2):
            return True
        else:
            return False


class Solution2:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))       