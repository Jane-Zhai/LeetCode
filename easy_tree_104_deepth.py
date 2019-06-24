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
    def maxDepth(self, root):
        """
        给定一个二叉树，找出其最大深度。
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1
        return max(left,right)
        

if __name__ == "__main__":
    t = [1,2,2,3,None,None,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])

    sol = Solution()
    print(sol.maxDepth(tt.root))