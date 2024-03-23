import java.util.*;

class ReorderList {
    public void reorderList(ListNode head) {
        Deque<Integer> vals = new LinkedList<>();
        ListNode temp = head;
        while(temp != null){
            vals.add(temp.val);
            temp = temp.next;
        }
        temp = head;
        boolean isEven = true;
        while(!vals.isEmpty()){
            if(isEven)
                temp.val = vals.removeFirst();
            else
                temp.val = vals.removeLast();
            isEven = !isEven;
            temp = temp.next;
        }
    }
}