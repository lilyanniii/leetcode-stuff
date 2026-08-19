class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        long_s = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                long_s = max(long_s, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return long_s