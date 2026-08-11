# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = l1
        list2 = l2

        dummy = ListNode()
        curr = dummy

        carry = 0

        while list1 and list2:
            val = list1.val + list2.val + carry

            if val > 9:
                new_node1 = ListNode()
                new_node1.val = val % 10

                carry = val // 10

                curr.next = new_node1
                curr = curr.next

            else:
                new_node = ListNode()
                new_node.val = val

                curr.next = new_node
                curr = curr.next

                carry = 0

            list1 = list1.next
            list2 = list2.next

        while list1:
            val = list1.val + carry
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
            list1 = list1.next

        while list2:
            val = list2.val + carry
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
            list2 = list2.next

        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node

        return dummy.next


        
