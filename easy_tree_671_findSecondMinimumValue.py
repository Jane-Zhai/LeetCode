# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        queue = [root]
        temp = []
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                if cur.left.val != cur.val:
                    temp.append(cur.left.val)
            if cur.right:
                queue.append(cur.right)
                if cur.right.val != cur.val:
                    temp.append(cur.right.val)
            if len(temp) == 2:
                return min(temp)
        return -1