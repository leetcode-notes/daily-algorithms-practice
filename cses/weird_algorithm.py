def solve(n):
    res = []
    while n != 1:
        res.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
    res.append(1)
    print(*res)


if __name__ == '__main__':
    n = int(input())
    solve(n)
