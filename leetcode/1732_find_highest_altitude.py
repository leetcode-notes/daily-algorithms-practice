class Solution:
    def largestAltitude(self, gain) -> int:
        cur_altitude = 0
        max_alt = 0
        for g in gain:
            cur_altitude += g
            max_alt = max(max_alt, cur_altitude)
        return max_alt


"""
Success
Details 
Runtime: 56 ms, faster than 13.51% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 14.2 MB, less than 73.05% of Python3 online submissions for Find the Highest Altitude.
Next challenges:
Missing Ranges
Max Chunks To Make Sorted II
Maximum Width Ramp
"""
