class TreeNode:
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        s = []
        if root.left is not None:
            s += [str(root.val) + '->' + t for t in self.binaryTreePaths(root.left)] 
        if root.right is not None:
            s += [str(root.val) + '->' + t for t in self.binaryTreePaths(root.right)] 
        return s
        

if __name__ == "__main__":
    t = [1,2,6,3,4,5,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])

    sol = Solution()
    print(sol.binaryTreePaths(tt.root))           