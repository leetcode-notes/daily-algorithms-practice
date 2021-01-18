class Solution:
    def solve(self, stacks, k):
        self.res = -2**32

        def rec(node, k, total):
            if k == 0:
                print(total+node)
                return total+node
            else:
                for stack in stacks:
                    if len(stack) > 0:
                        cur = stack.pop()
                        rec(cur, k-1, total+node)
            return

        cc = rec(stacks[2][-1], k, 0)


s = Solution()
print(s.solve([[1, 2, 4],
               [2, 3, 5],
               [3, 0, 6]], 3))
