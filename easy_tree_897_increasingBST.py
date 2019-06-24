# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
    def increasingBST(self, root):
        
        def order(root):
            if root is None:
                return []
            return order(root.left)+[root]+order(root.right)

        queue = order(root)
        root = queue[0]
        cur = root
        for node in queue[1:]:
            cur.left = None
            cur.right = node
            cur = cur.right 
        return root


    def increasingBST2(self, root, tail = None):
            if not root: return tail
            res = self.increasingBST2(root.left, root)
            root.left = None
            root.right = self.increasingBST2(root.right, tail)
            return res


