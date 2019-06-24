class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
        如果有两个中间结点，则返回第二个中间结点。
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        

data = [1,2,3,5,4,1]
head = ListNode(data[0])
cur = head
for i in data[1:]:
    cur.next = ListNode(i) 
    cur = cur.next

res = Solution().middleNode(head)
print(res.val)