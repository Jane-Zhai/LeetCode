class ListNode:
    def __init__(self,node=None):
        self.val = node
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
        """
        cur = head   
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head.next
        while q:
            if q.val == p.val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return head


if __name__ == "__main__":
    root = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    root.next = node1
    node1.next = node2
    node2.next = node3

    res = Solution().deleteDuplicates(root)
    while res:
        print(res.val)
        res = res.next