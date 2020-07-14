def solve(row):
    count = 0
    prev_max = row[0]
    if len(row) == 1:
        return 1 
    for i in range(len(row)):
        if i == 0 and len(row) > 1:
            if row[i] > row[i+1]:
                count += 1
        if row[i] > prev_max:
            if i == len(row)-1:
                count += 1
            else:
                if row[i] > row[i+1]:
                    count += 1
        prev_max = max(prev_max, row[i])
    return count


cases = int(input())
for i in range(1, cases+1):
    n = int(input())
    row = [int(s) for s in input().split(" ")]
    ans = solve(row)
    print("Case #{}: {}".format(i, ans))