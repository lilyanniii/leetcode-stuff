class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def copy_list(head):
            dummy = ListNode()
            copy_curr = dummy
            curr = head
            while curr:
                copy_curr.next = ListNode(curr.val)
                copy_curr = copy_curr.next
                curr = curr.next
            return dummy.next

        original = copy_list(head)

        # get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # position from the front
        target_index = length - n

        # remove from copy at that index
        dummy = ListNode(0, original)
        curr = dummy
        for i in range(target_index):
            curr = curr.next
        curr.next = curr.next.next

        return dummy.next