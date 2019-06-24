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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        s = 0
        if root.left is not None:
            s += root.left.val + self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            s += self.sumOfLeftLeaves(root.right)
        return s

class Solution2(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)  # isn't leave


if __name__ == "__main__":
    t = [1,2,6,3,4,5,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])

    sol = Solution()
    print(sol.sumOfLeftLeaves(tt.root))           