def solve(n, inbound, outbound):
    p = [["N"]*n for _ in range(n)]
    for i in range(n):
        p[i][i] = 'Y'

    i = 0
    while i < n:
        for row in p:
            for j in range(i+1, n):
                if row[j-1] == 'N':
                    break
                if row[j-1] == 'Y' and inbound[j] == 'Y' and outbound[j-1] == 'Y':
                    row[j] = 'Y'
        i += 1
    i = 0
    while i < n:
        for row in p:
            for j in range(i-1, -1, -1):
                if row[j+1] == 'N':
                    break
                if row[j+1] == 'Y' and outbound[j+1] == 'Y' and inbound[j] == 'Y':
                    row[j] = 'Y'
        i += 1
    return p


# n = int(input())
# i = 0
# while i < n:
#     a = int(input())
#     ib = input()
#     ob = input()
#     ans = solve(a, ib, ob)
#     print("Case #{}".format(i+1))
#     for line in ans:
#         print("".join(c for c in line))
#     i += 1
g = open('output3.txt', 'w')
with open('sample.txt', 'r') as f:
    num_cases = int(f.readline())
    for i in range(num_cases):
        a = int(f.readline())
        ip = (f.readline())
        op = f.readline()
        res = solve(a, ip, op)
        g.write("Case #{}:".format(i+1)+"\n")
        for line in res:
            g.write("".join(c for c in line)+"\n")
    f.close()
    g.close()

'''
N = 10
ib = "NYYYNNYYYY"
ob = "YYNYYNYYNY"
solve(10, ib, ob)
'''

# def solve(n):
#     if n == 1:
#         return 3
#     if n == 2:
#         return 1
#     if n >= 3:
#         return 2*solve(n-1)-solve(n-2)

# print(solve(4))
