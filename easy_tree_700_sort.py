# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.val == val:
                return cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return None
        