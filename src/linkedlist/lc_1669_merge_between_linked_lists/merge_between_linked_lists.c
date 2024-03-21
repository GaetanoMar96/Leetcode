/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){
    struct ListNode* temp;
    struct ListNode* temp1 = list1;
    struct ListNode* temp2 = list2;
    int count = 0;
    while(temp1->next != NULL)
    {
        if(count == a - 1)
        {
            temp = temp1;
            while(count < b)
            {
                temp = temp->next;
                count++;
            }
            temp1->next = list2;
            while(temp2->next != NULL)
            {
                temp2 = temp2-> next;
            }
            temp2->next = temp->next;
            free(temp);
            
        }
        else{
            count++;
            temp1 = temp1->next;
        }
        
    }
    return list1;
}