
struct ListNode {
   int val;
   struct ListNode *next;
};
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (dummy == NULL)
        return NULL;
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* temp1 = dummy;
    struct ListNode* temp2 = head;
    
    for(int i = 0; i < n; i++)
        temp2 = temp2->next;
    
    while(temp2 != NULL){
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    
    temp1->next = temp1->next->next;
    return dummy->next;
    
}