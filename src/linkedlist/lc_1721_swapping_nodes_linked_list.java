class Solution {

    static class ListNode {
        int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode swapNodes(ListNode head, int k) {
        ListNode temp = head;
        int length = 0;
        while (temp != null) {
            temp = temp.next;
            length++;
        }
        temp = head;
        ListNode temp2 = null;
        ListNode temp1 = null;
        int i = 1;
        while (temp != null) {
            if (i == k) {
                temp1 = temp;
            }
            if (i == (length - k + 1)) {
                temp2 = temp;
            }
            temp = temp.next;
            i++;
        }
        int v = temp2.val;
        temp2.val = temp1.val;
        temp1.val = v;
        return head;
    }
}