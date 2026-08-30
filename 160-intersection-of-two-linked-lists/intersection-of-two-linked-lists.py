# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        pointer2 = headB
        visitted = {}
        count = 0

        while(pointer1 is not None) :
           visitted[pointer1] = True
           pointer1 = pointer1.next
        
        while(pointer2 is not None):
            if(pointer2 in visitted):
                return pointer2
            pointer2 = pointer2.next

        return None
            