# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #split the linked list into two
        second = slow.next
        slow.next = None


        #reverse the second linked list

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #reorder

        while head and prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            head = tmp1

            prev.next = head
            prev = tmp2
            