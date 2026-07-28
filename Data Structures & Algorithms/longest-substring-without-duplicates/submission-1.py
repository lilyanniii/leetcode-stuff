class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l, r = 0, 1
        table = set()


        for r in range(len(s)):

            while s[r] in table:
                table.remove(s[l])
                l += 1
            
            table.add(s[r])
            count = max(count, r - l + 1)
                

        return count


