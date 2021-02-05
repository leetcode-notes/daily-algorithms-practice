class Solution:
    def isPalindrome(self, head) -> bool:
        forward = []
        while head:
            forward.append(head.val)
            head = head.next
        return forward == forward[::-1]


"""
Success
Details 
Runtime: 124 ms, faster than 6.12% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.6 MB, less than 20.68% of Python3 online submissions for Palindrome Linked List.
Next challenges:
Reverse Linked List
"""
