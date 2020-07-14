def solve(row):
    length = 1
    up, down = False, False
    count = 0
    for i in range(1, len(row)):
        if length > 4:
            count += 1
            length = 1
        if row[i] > row[i-1]:
            if down:
                down = False
                length = 0
            length += 1
            up = True
        elif row[i] < row[i-1]:
            if up:
                up = False
                length = 0
            length += 1
            down = True
    if length > 4:
        count += 1
    return count


cases = int(input())
for i in range(1, cases+1):
    n = int(input())
    row = [int(s) for s in input().split(" ")]
    ans = solve(row)
    print("Case #{}: {}".format(i, ans))
