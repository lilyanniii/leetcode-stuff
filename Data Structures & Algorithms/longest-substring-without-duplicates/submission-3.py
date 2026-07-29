class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()
        l, r = 0, 0
        long_s = 0

        while r < len(s):
            if s[r] not in table:
                table.add(s[r])
                r += 1
                long_s = max(long_s, r - l)
            else:
                table.remove(s[l])
                l += 1
                
            
        return long_s