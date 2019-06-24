class ListNode():
    def __init__(self, node=None):
        self.val = node
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        给定一个链表，判断链表中是否有环。
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1，则在该链表中没有环。
        """
        if not head:
            return False
        walker = head
        runner = head.next
        try:
            while walker != runner:
                walker = walker.next
                print(walker.val)
                runner = runner.next.next
                print(runner.val)
            return True
        except:
            return False


node0 = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = None
res = Solution().hasCycle(node0)
print(res)