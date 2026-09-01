# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remember = 0
        dummy = ListNode(0)
        current = dummy

        while(l1 != None or l2 != None or remember > 0):
            sum = remember

            if(l1 != None):
                sum += l1.val
                l1 = l1.next
            if(l2 != None):
                sum +=l2.val
                l2 = l2.next

            remember = sum//10
            current.next = ListNode(sum%10)
            current = current.next
        
        return dummy.next