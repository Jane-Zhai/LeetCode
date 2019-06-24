class ListNode:
    def __init__(self,node=None):
        self.val = node
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        反转一个单链表。
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        q = head.next
        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next
        return p


data = [1,2,3,4,5,6]
head = ListNode(data[0])
cur = head
for i in data[1:]:
    cur.next = ListNode(i) 
    cur = cur.next

res = Solution().reverseList(head)

cur = res
while cur:
    print(cur.val, end=" ")
    cur = cur.next
print("")