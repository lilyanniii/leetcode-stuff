# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f, s = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        #now have two lists
        second_l = s.next
        s.next = None
        
        #revers second linked list
        curr = second_l
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        while head and prev:
            temp1L = head.next
            temp2L = prev.next

            head.next = prev
            head = temp1L
            prev.next = head

            prev = temp2L


            


            



            