/** Definition for singly-linked list.*/
 public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pt1, pt2;
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        pt1 = l1;
        pt2 = l2;
        int rem = 0;
        while (pt1 != null && pt2 != null) {
            int val = pt1.val + pt2.val + rem;
            if (val > 9) {
                val = val % 10;
                rem = 1;
            } else {
                rem = 0;
            }
            
            ListNode node = new ListNode(val);
            curr.next = node;
            curr = curr.next;
            pt1 = pt1.next;
            pt2 = pt2.next;
        }
        while (pt1 != null) {
            int val = pt1.val + rem;
            if (val > 9) {
                val = val % 10;
                rem = 1;
            } else {
                rem = 0;
            }
            ListNode node = new ListNode(val);
            curr.next = node;
            curr = curr.next;
            pt1 = pt1.next;
        }
        while (pt2 != null) {
            int val = pt2.val + rem;
            if (val > 9) {
                val = val % 10;
                rem = 1;
            } else {
                rem = 0;
            }
            ListNode node = new ListNode(val);
            curr.next = node;
            curr = curr.next;
            pt2 = pt2.next;
        }
        if (rem == 1) {
            curr.next = new ListNode(1, null);
        }
        return dummy.next;
    }
}