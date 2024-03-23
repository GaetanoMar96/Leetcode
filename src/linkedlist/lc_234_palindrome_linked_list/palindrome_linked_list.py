from listNode import ListNode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            t = head
            t1, t2 = None, None
            while t:
                t1 = t
                t = t.next
                t1.next = t2
                t2 = t1
            return t1
        
        if not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        temp = slow.next
        slow.next = None
        rev = reverse(temp)
        t1, t2 = head, rev
        while t1 and t2:
            if t1.val != t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return True