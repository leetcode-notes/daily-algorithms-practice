n = int(input())
s = input()


def solve(n, s):
    count = 0
    for c in s:
        if c == 'A':
            count += 1
    if count > n - count:
        print("Anton")
    elif count < n - count:
        print("Danik")
    else:
        print("Friendship")


solve(n, s)
