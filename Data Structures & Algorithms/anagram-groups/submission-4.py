class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            count = [0] * 26    
            for c in s:
                count[ord(c) - ord('a')] += 1
            table[tuple(count)].append(s)
        
        return list(table.values())
                