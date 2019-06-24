class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self,item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return
        
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


class Solution(object):
    def isBalanced(self, root):
        """
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        :type root: TreeNode
        :rtype: bool
        """
        def depth(self,node):
            if node is None:
                return 0
            return max(self.height(node.left),self.height(node.right))+1
        
        if root is None:
            return True
        if abs(depth(root.left)-depth(root.right)) >= 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)