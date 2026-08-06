# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_p = head
        fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next


        #reversing second half of the linked list to be its own
        prev = None
        curr = slow_p.next

        slow_p.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        while head and prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp

            prev = temp2
            head = temp
    
        

