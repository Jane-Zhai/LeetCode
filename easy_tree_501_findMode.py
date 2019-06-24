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
    def findMode(self, root):
        """
        给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
        假定 BST 有如下定义：
            结点左子树中所含结点的值小于等于当前结点的值
            结点右子树中所含结点的值大于等于当前结点的值
            左子树和右子树都是二叉搜索树
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        dic = dict()
        queue = [root]
        while queue:
            cur = queue.pop(0)
            dic[cur.val] = dic.get(cur.val,0)+1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res = []
        maxele = max(dic.values())
        for key,val in dic.items():
            if val == maxele:
                res.append(key)
        return res
            
        
        

if __name__ == "__main__":
    t = [1,2,3,2]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution()
    print(sol.findMode(tt.root))
        