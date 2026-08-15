# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast and slow pointer to determine the mid point then reverse the second linked list

        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next

        #now have two lists list2 and s
        list2 = s.next
        s.next = None

        #reverse the second list
        prev = None

        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt

        while head and prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            head = tmp1

            prev.next = head
            prev = tmp2
        







        #add ~2 min to the end time 