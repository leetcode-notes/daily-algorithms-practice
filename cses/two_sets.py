def solve(n):
    total = (n*(n+1))//2
    if total % 2 == 1:
        print("NO")
    if n % 2 == 0:
        left, right = 1, n
        first, second = [], []
        while left < right:
            first.append(left)
            first.append(right)
            left += 1
            right -= 1
            second.append(left)
            second.append(right)
            left += 1
            right -= 1

        print(*first)
        print(*second)


if __name__ == '__main__':
    n = int(input())
    solve(n)
