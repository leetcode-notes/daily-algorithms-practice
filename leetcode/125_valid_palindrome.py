class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""
        i = len(s)-1
        cleaned = ""
        for c in s:
            if c.isalnum():
                if c.isalpha():
                    cleaned += c.lower()
                else:
                    cleaned += c
        while i >= 0:
            if s[i].isalnum():
                if s[i].isalpha():
                    reversed += s[i].lower()
                else:
                    reversed += s[i]
            i -= 1
        return reversed == cleaned


"""
Success
Details 
Runtime: 108 ms, faster than 5.96% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.7 MB, less than 50.34% of Python3 online submissions for Valid Palindrome.
Next challenges:
Palindrome Linked List
Valid Palindrome II
"""
