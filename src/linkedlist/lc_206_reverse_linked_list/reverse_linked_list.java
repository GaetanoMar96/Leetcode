class Solution {
    static class ListNode {
        int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    public ListNode reverseList(ListNode head) {
        ListNode temp1 = head;
        ListNode temp2;
        ListNode temp3 = null;

        while(temp1 != null) {
            temp2 = temp1;
            temp1 = temp1.next;
            temp2.next = temp3;
            temp3 = temp2;
        }
        return temp3;
    }
}