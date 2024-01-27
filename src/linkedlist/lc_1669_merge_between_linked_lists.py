from listNode import ListNode

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        temp = list1
        tempprev = dummy
        start = None

        temp2 = list2
        while temp2.next:
            temp2 = temp2.next
        i = 0
        while True:
            if i == a:
                start = tempprev
            if i == b:
                temp2.next = temp.next
                break
            temp = temp.next
            tempprev = tempprev.next
            i += 1
        start.next = list2
        return dummy.next