class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        p_hash = [0]*26
        for ch in p:
            p_hash[ord(ch)-97] += 1
        s_hash = [0] * 26
        for ch in s[0:len(p)]:
            s_hash[ord(ch)-97] += 1

        left, right = 0, len(p) - 1

        while right < len(s):
            if p_hash == s_hash:
                res.append(left)
            right += 1
            if right < len(s):
                s_hash[ord(s[left])-97] -= 1
                s_hash[ord(s[right])-97] += 1
            left += 1
        return res


"""
Success
Details 
Runtime: 104 ms, faster than 92.91% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15 MB, less than 92.16% of Python3 online submissions for Find All Anagrams in a String.
Next challenges:
Permutation in String
"""
