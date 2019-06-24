class TreeNode(object):
    def __init__(self, x):
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
    def __init__(self):
        self.tilt = 0
        self.leftsum = 0
        self.rightsum = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,ans = self.sumTree(root)
        return ans

    def sumTree(self,node):
        if not node:
            return 0,0
        left,ans1 = self.sumTree(node.left)
        right,ans2 = self.sumTree(node.right)
        return node.val+left+right,abs(right-left)+ans1+ans2
        

if __name__ == "__main__":
    t = [1,2,3,4,5,6,8]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution()
    print(sol.findTilt(tt.root))