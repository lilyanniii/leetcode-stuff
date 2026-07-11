class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        first_string = sorted(s)
        second_string = sorted(t)

        for i in range(s_length):
            if first_string[i] != second_string[i]:
                return False
            
        return True
        