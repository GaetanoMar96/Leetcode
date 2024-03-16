from listNode import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        temp = head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False