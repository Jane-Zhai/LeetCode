# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pathNum = 0
    def pathSum(self, root, sum):
        """
        给定一个二叉树，它的每个结点都存放着一个整数值。
        找出路径和等于给定数值的路径总数。
        路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
        二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root,s):
            if root is None:
                return
            if s == root.val:
                self.pathNum += 1
            dfs(root.left, s-root.val)
            dfs(root.right,s-root.val)

        if root is None:
            return 0
        dfs(root,sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.pathNum
        

class Solution2(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self, node, sum):
        if not node:
            return 0
        return (1 if node.val == sum else 0) + self.pathSumFrom(node.left, sum - node.val) + self.pathSumFrom(node.right, sum - node.val)