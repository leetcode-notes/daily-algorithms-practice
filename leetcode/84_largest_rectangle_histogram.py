class Solution:
    def largestRectangleArea(self, heights) -> int:
        ans, stack = 0, []
        for i, h in enumerate(heights+[0]):

            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1]-1
                else:
                    width = i
                ans = max(ans, height*width)
            stack.append(i)
        return ans


"""
Success
Details
Runtime: 808 ms, faster than 25.90 % of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 27.1 MB, less than 43.00 % of Python3 online submissions for Largest Rectangle in Histogram.
Next challenges:
Maximal Rectangle
Maximum Score of a Good Subarray
"""
