class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer, One pointer at the beginning of the string, one pointer at the end of the
        # string and they move towards the middle and while moving to wards the middle, they are checking
        # if the letters are the same.
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer].isalnum():
                if s[right_pointer].isalnum():
                    if s[left_pointer].lower() == s[right_pointer].lower():
                        left_pointer += 1
                        right_pointer -= 1
                    else:
                        return False
                else:
                    right_pointer -= 1
            else:
                left_pointer += 1    
        
        return True
