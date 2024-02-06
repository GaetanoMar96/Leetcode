from listNode import ListNode

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        temp = head
        stack = []
        while temp:
            val = temp.val
            if not stack:
                stack.append(val)
                temp = temp.next
                continue
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)
            temp = temp.next
        dummy = ListNode(-1)
        temp = dummy
        while stack:
            val = stack.pop(0)
            node = ListNode(val)
            temp.next = node
            temp = temp.next
        return dummy.next