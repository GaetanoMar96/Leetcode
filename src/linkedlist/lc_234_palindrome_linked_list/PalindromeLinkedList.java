class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        List<Integer> list = new ArrayList<>();
        ListNode temp = head;
        while (temp != null) {
            list.add(temp.val);
            temp = temp.next;
        }

        int l, r;
        l = 0;
        r = list.size() - 1;
        while (l <= r){
            if (list.get(l) != list.get(r))
                return false;
            l++;
            r--;
        }
        return true;
    }
}