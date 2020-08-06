class Solution:
    def getWinner(self, arr, k) -> int:
        start = arr[0]
        count = 0
        if k >= len(arr):
            return max(arr)

        def play(arr):
            if arr[0] > arr[1]:
                winner = arr[0]
                temp = arr.pop(1)
            else:
                winner = arr[1]
                temp = arr.pop(0)
            arr.append(temp)
            return winner
        while True:
            cur = play(arr)

            if cur == start:
                count += 1
            else:
                start = cur
                count = 1
            if count == k:
                return cur


'''
Success
Details
Runtime: 5596 ms, faster than 25.00% of Python3
Memory Usage: 27.5 MB, less than 100.00% of Python3
Next challenges:
Find All Duplicates in an Array
Replace Elements with Greatest Element on Right Side
Check If Array Pairs Are Divisible by k
'''
