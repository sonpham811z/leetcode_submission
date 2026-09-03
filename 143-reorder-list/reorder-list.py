# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # cắt đôi linkedlist
        begin_of_second = slow.next
        slow.next = None

        prev = None
        curr = begin_of_second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head2 = prev

        while head2:
            tmp1 = head.next
            tmp2 = head2.next

            head.next = head2
            head = tmp1
            head2.next=head
            head2 = tmp2

        
        