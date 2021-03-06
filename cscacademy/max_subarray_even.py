'''
Given an array of N elements. Find the maximum sum of a subarray having even
length.
'''


def max_subarray_even_length(arr):
    n = len(arr)
    dp = [0] * (n+2)
    res = -float('inf')
    for i in range(1, n):
        dp[n-i-1] = arr[n-i-1] + arr[n-i] + dp[n-i+1]
        if dp[n-i-1] > res:
            res = dp[n-i-1]
        dp[n-i-1] = max(0, dp[n-i-1])
    print(dp)
    return res


print(max_subarray_even_length([8, 9, -8, 9, 10]))
