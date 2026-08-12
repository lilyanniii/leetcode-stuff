# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #phase 1 is to split the linked list into two separate list:
        curr = head
        s, f = curr, curr

        while f and f.next:
            s = s.next
            f = f.next.next
            

        second = s.next
        s.next = None

        #reverse the second linked list
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        while head and prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            head = tmp1

            prev.next = head
            prev = tmp2





