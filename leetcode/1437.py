class Solution:
    def kLengthApart(self, nums, k):
        dist = 0 
        for i, elt in enumerate(nums):
            if elt == 0:
                dist += 1 
            if elt == 1 and i !=0:
                if dist < k:
                    return False
                dist = 0 
        return True 
