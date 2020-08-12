from functools import lru_cache


def solve(n):
    if n == 0 or n == 1:
        return 1
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, 7):
            if j <= i:
                dp[i] = (dp[i] + dp[i-j]) % (10**9+7)
    return dp[-1] % (10**9+7)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))


@lru_cache(maxsize=None)
def diceSum(n):
    total = 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        for i in range(1, 7):
            if i <= n:
                total += diceSum(n-i)
    return total
