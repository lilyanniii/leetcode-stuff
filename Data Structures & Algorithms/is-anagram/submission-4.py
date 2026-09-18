class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have two hashmaps that contains the count of each letter in both inputs.
        #if they have same count, return True, otherwise False

        #first hash map
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1

        for c in t:
            arr[ord(c) - ord('a')] -= 1
        

        return all(x == 0 for x in arr)
        


        
