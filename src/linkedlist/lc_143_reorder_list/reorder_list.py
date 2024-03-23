from listNode import ListNode
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
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

        if not head.next:
            return head
        
        slow = head
        fast = head
        while fast:
            temp = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            
        temp.next = None
        slow = reverse(slow)
        
        temp1 = head
        temp2 = None
        slow2 = None
        start = True
        while temp1 and slow:
            if start:
                temp2 = temp1.next
                temp1.next = slow
                temp1 = temp2
                start = False
            else:
                slow2 = slow.next
                slow.next = temp1
                slow = slow2
                start = True
        

            
            
        


                
            
        
        
        