"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        curr = head


        #first pass, copy the nodes
        while curr:
            copy = Node(curr.val)
            hash_map[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = hash_map[curr]
            copy.next = hash_map.get(curr.next)
            copy.random = hash_map.get(curr.random)
            
            curr = curr.next

        return hash_map.get(head)
        
        

