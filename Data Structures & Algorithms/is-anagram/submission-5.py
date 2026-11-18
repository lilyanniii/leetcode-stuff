class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #go through first array and add 1 to each unique character. Go through second array and subtract 1 for each unique character. if the value of all characters != 0 return False, otherwise return true.

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False

        return True
        