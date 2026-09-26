/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* res = head;
        if (!head || !head->next) {
            return head;
        }

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        while(prev->next && prev->next->next)
        {
           ListNode* curr = prev->next;
           ListNode* nextNode = curr->next;

            curr->next = nextNode->next;
            nextNode->next = curr;
            prev->next = nextNode;

            prev = curr;
        }

        return dummy.next;

    }
};