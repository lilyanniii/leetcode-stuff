class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        tables1 = {}

        for ch in s1:
            if ch in tables1:
                tables1[ch] += 1
            else:
                tables1[ch] = 1
        
        tables2 = {}

        if len(s1) > len(s2):
            return False

        l, r = 0, 0

        while r < len(s2):

           
            if s2[r] not in tables2:
                tables2[s2[r]] = 1
                r += 1
            else:
                tables2[s2[r]] += 1
                r += 1

            if r - l == len(s1):
                if tables2 == tables1:
                    return True
                tables2[s2[l]] -= 1
                if tables2[s2[l]] == 0:
                    del tables2[s2[l]]
                l += 1
        
        return res
                
            
                

