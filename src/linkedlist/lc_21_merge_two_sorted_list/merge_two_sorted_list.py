from listNode import ListNode
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        p1, p2 = list1, list2
        dummy = ListNode(0)
        temp = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                temp.next = ListNode(p1.val)
                p1 = p1.next
            else:
                temp.next = ListNode(p2.val)
                p2 = p2.next
            temp = temp.next
        if p1:
            while p1:
                temp.next = ListNode(p1.val)
                p1 = p1.next
                temp = temp.next
        if p2:
            while p2:
                temp.next = ListNode(p2.val)
                p2 = p2.next
                temp = temp.next
        return dummy.next