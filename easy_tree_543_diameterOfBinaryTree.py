class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.num = 0
    def diameterOfBinaryTree(self, root):
        """
        给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if root is None:
                return 0
            return max(depth(root.left),depth(root.right)) + 1
        if root is None:
            return 0
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        self.num = max(self.num,depth(root.left)+depth(root.right))
        return self.num
