class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        in_degrees = {}
        res = []
        for u, v in edges:
            in_degrees[v] = in_degrees.get(v, 0)+1
        for i in range(n):
            if in_degrees.get(i, 0) < 1:
                res.append(i)
        return res


"""
Success
Details 
Runtime: 1236 ms, faster than 29.49% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 53.2 MB, less than 46.36% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Next challenges:
Reconstruct Itinerary
Network Delay Time
String Transforms Into Another String
"""
