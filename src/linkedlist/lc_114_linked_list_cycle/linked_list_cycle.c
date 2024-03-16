bool hasCycle(struct ListNode *head) {
    if (head == NULL)
        return false;
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;
    while(fast != NULL){
        if (fast == slow)
            return true;
        slow = slow->next;
        fast = fast->next;
        if (fast != NULL)
            fast = fast->next;
    }
    return false;
}