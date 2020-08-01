from collections import Counter


def solve(n, nums):
    d = Counter(nums)
    for i in range(1, n+1):
        if i not in d:
            return i


n = int(input())
nums = [int(i) for i in input().split(" ")]
print(solve(n, nums))
