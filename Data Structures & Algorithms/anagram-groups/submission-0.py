class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for words in strs:
            sorted_text = "".join(sorted(words))
            if sorted_text in hash_table:
                hash_table[sorted_text].append(words)
            else:
                hash_table[sorted_text] = [words]

        return list(hash_table.values()) 