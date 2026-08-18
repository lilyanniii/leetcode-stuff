# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        list1, list2 = l1, l2

        while list1 and list2:
            val = list1.val + list2.val + carry

            carry = val // 10
            val = val % 10
            
            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next

            list1 = list1.next
            list2 = list2.next

        while list1:
            val = list1.val + carry
            carry = val // 10
            val = val % 10
            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next
            list1 = list1.next

        while list2:
            val = list2.val + carry
            carry = val // 10
            val = val % 10
            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next
            list2 = list2.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next