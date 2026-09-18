class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have two hashmaps that contains the count of each letter in both inputs.
        #if they have same count, return True, otherwise False

        #first hash map

        return Counter(s) == Counter(t)
        


        
