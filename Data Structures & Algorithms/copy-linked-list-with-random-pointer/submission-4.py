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
        curr = head

        hash_map = {}

        #iterate over one time to create a hashmap of all the nodes:
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copy = hash_map[curr]
            copy.next = hash_map.get(curr.next)
            copy.random = hash_map.get(curr.random)
            curr = curr.next
        
        return hash_map.get(head)