from listNode import ListNode
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p1 = head
        p2, p3 = None, None

        while p1:
            p2 = p1
            p1 = p1.next
            p2.next = p3
            p3 = p2
        head = p3
        return head
        