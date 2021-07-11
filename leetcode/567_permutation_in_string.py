class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = [0] * 26
        s2_hash = [0] * 26
        for ch in s1:
            s1_hash[ord(ch)-97] += 1
        for ch in s2[0:len(s1)]:
            s2_hash[ord(ch)-97] += 1

        left, right = 0, len(s1)-1

        while right < len(s2):
            if s1_hash == s2_hash:
                return True
            right += 1
            if right < len(s2):
                s2_hash[ord(s2[right])-97] += 1
                s2_hash[ord(s2[left])-97] -= 1
            left += 1
        return False


"""
Success
Details 
Runtime: 64 ms, faster than 86.69% of Python3 online submissions for Permutation in String.
Memory Usage: 14.5 MB, less than 8.08% of Python3 online submissions for Permutation in String.
Next challenges:
Minimum Window Substring
"""
