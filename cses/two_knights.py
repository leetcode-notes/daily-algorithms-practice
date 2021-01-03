def solve(n):
    for i in range(1, n+1):
        total_positions = (i**2*(i**2-1))//2
        attacking_positions = 4*(i-1)*(i-2)
        print(total_positions-attacking_positions)


if __name__ == '__main__':
    n = int(input())
    solve(n)

'''
https://math.stackexchange.com/questions/3266257/number-of-ways-two-knights-can-be-placed-such-that-they-dont-attack/3266324#3266324
'''
