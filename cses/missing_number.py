from collections import Counter


def solve(n, nums):
    d = Counter(nums)
    for i in range(1, n+1):
        if i not in d:
            print(i)
            return


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    solve(n, nums)
