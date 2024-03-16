from listNode import ListNode
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow