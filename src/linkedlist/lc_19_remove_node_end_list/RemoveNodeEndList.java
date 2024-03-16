class RemoveNodeEndList {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode temp = head;
        while(temp != null) {
            temp = temp.next;
            size++;
        }
        int target = size - n;
        if(target == 0) {
            return head.next;
        }
        
        int curr = 0;
        temp = head;
        ListNode temp1 = null;
        while(temp != null) {
            if (curr == target) {
                temp1.next = temp.next;
                break;
            }
            temp1 = temp;
            temp = temp.next;
            curr++;
        }
        return head;
    }
}