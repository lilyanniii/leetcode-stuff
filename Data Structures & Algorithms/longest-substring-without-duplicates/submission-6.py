class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_s = 0
        seen = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                long_s = max(long_s, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
                
        return long_s