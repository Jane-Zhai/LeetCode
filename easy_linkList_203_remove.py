class ListNode:
    def __init__(self,node=None):
        self.val = node
        self.next = None

class Solution:
    def removeElements(self,head,val):
        """
        删除链表中等于给定值 val 的所有节点。
        """
        if head.val == val:
            head = head.next
        cur = head
        while cur:
            if val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


data = [6,2,6,3,4,5,6]
head = ListNode(data[0])
cur = head
for i in data[1:]:
    cur.next = ListNode(i) 
    cur = cur.next

res = Solution().removeElements(head,6)

cur = res
while cur:
    print(cur.val, end=" ")
    cur = cur.next
print("")