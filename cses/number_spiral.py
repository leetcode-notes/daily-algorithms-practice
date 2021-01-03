def solve(r, c):

    if r == c:
        print(diag(r))
        return
    else:
        critical = max(r, c)
        res = diag(critical)
        if critical % 2 == 1:
            if critical == r:
                print(res-(critical-c))
            elif critical == c:
                print(res+(critical-r))
        else:
            if critical == r:
                print(res+(critical-c))
            else:
                print(res-(critical-r))


def diag(n):
    if n == 1:
        return 1
    return (n-1)**2 + n


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        nums = [int(i) for i in input().split(" ")]
        r, c = nums[0], nums[1]
        solve(r, c)
        n -= 1
