def solve(arr):
    prev_diff = arr[0]-arr[1]
    max_len = 2
    cur_len = 2
    for i in range(1, len(arr)-1):
        cur_diff = arr[i] - arr[i+1]
        if cur_diff != prev_diff:
            cur_len = 2
            prev_diff = cur_diff
        else:
            cur_len += 1
        max_len = max(max_len, cur_len)
    return max_len


cases = int(input())
for i in range(1, cases+1):
    n = int(input())
    row = [int(s) for s in input().split(" ")]
    ans = solve(row)
    print("Case #{}: {}".format(i, ans))
