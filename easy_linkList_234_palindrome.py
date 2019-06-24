class ListNode:
    def __init__(self,node=None):
        self.val = node
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        请判断一个链表是否为回文链表。
        :type head: ListNode
        :rtype: bool
        """
        # 快慢指针找到链表长度的一半
        slow = fast = head
        while fast and fast.next: # 链表长度偶/奇
            slow = slow.next
            fast = fast.next.next

        # 翻转后半部分
        rev = None
        while slow:
            rev, rev.next, slow = slow, rev, slow.next 

        # 比较
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True


data = [1,2,3,4,1]
head = ListNode(data[0])
cur = head
for i in data[1:]:
    cur.next = ListNode(i) 
    cur = cur.next

res = Solution().isPalindrome(head)
print(res)
# cur = res
# while cur:
#     print(cur.val, end=" ")
#     cur = cur.next
# print("")