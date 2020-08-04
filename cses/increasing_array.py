def solve(arr):
    total = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            total += arr[i-1] - arr[i]
            arr[i] = arr[i-1]

    print(total)


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    solve(nums)
