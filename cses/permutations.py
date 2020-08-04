def solve(n):
    if n == 2 or n == 3:
        print("NO SOLUTION")
    res = []
    for i in range(2, n+1, 2):
        res.append(i)
    for i in range(1, n+1, 2):
        res.append(i)
    print(*res)


if __name__ == '__main__':
    n = int(input())
    solve(n)
