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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = [root]
        temp = list()
        while queue:
            cur = queue.pop(0)
            for i in temp:
                if cur.val == k-i:
                    return True
            temp.append(cur.val)

            if cur:
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return False


if __name__ == "__main__":
    t = [5,3,6,2,4,7]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution()
    print(sol.findTarget(tt.root,9))
        