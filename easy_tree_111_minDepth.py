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
    def minDepth(self, root):
        """
        给定一个二叉树，找出其最小深度。
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.right:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        elif root.left:
            return 1+self.minDepth(root.left)
        elif root.right:
            return 1+self.minDepth(root.right)
        else:
            return 1


class Solution2(object):
    def minDepth(self, root):
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left,right)+1 if left and right else left+right+1


if __name__ == "__main__":
    t = [1,2]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution2()
    print(sol.minDepth(tt.root))
        