from collections import deque


class Solution:
    def countStudents(self, students, sandwiches):
        pq, sq = deque(), deque()
        for s in students:
            pq.append(s)
        for sw in sandwiches:
            sq.append(sw)

        ate = 0
        i = 0
        while pq and sq:
            i += 1
            if i > len(students)*5:
                break
            if pq[0] == sq[0]:
                pq.popleft()
                sq.popleft()
                ate += 1
            else:
                cur = pq.popleft()
                pq.append(cur)

        return len(students)-ate


"""
Success
Details
Runtime: 36 ms, faster than 100.00% of Python3 online submissions
for Number of Students Unable to Eat Lunch.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions
for Number of Students Unable to Eat Lunch.
Next challenges:
Maximum Sum of 3 Non-Overlapping Subarrays
Two Sum Less Than K
Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
"""
