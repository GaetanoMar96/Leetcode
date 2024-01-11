from listNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0, None)
        temp = dummy
        t1, t2 = l1, l2
        rem = 0

        while t1 and t2:
            v1 = t1.val
            v2 = t2.val
            v = v1 + v2
            if rem > 0:
                v += rem
            if v // 10 > 0:
                rem = 1
                v = v % 10
            else:
                rem = 0
            
            newNode = ListNode(v, None)
            temp.next = newNode
            temp = temp.next
            t1 = t1.next
            t2 = t2.next
        while t1:
            v = t1.val
            if rem > 0:
                v += rem
            if v // 10 > 0:
                rem = 1
                v = v % 10
            else:
                rem = 0
            newNode = ListNode(v, None)
            temp.next = newNode
            temp = temp.next
            
            t1 = t1.next
        while t2:
            v = t2.val
            if rem > 0:
                v += rem
            if v // 10 > 0:
                rem = 1
                v = v % 10
            else:
                rem = 0
            newNode = ListNode(v, None)
            temp.next = newNode
            temp = temp.next
            
            t2 = t2.next
        if rem > 0:
            newNode = ListNode(rem, None)
            temp.next = newNode
        return dummy.next
        
           