from listNode import ListNode
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        idx = len(vals) - n
        vals.pop(idx)
        prev = None
        while vals:
            node = ListNode(vals.pop(), prev)
            prev = node
        return prev
        