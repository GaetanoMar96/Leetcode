from listNode import ListNode
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1, list1)
        count = 0
        temp2 = list2
        #temp2 at end of list 2
        while temp2.next:
            temp2 = temp2.next
        tempa = None
        tempb = None
        temp = list1
        while temp:
            if count == a - 1:
                tempa = temp
                break
            temp = temp.next
            count += 1
        while temp:
            if count == b:
                tempb = temp
                break
            temp = temp.next
            count += 1
        tempa.next = list2
        temp2.next = tempb.next
        return dummy.next
            
        