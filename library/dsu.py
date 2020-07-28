class Solution:
    def findKthLargest(self, nums, k):
        return quick_select(nums, 0, len(nums)-1, k-1)


def quick_select(nums, l, r, k):
    if l > r:
        return nums[k]
    s, e = l, r
    pi = random.randint(l, r)
    pivot = nums[pi]
    while l <= r:
        while l <= r and nums[r] < pivot:
            r -= 1
        while l <= r and nums[l] > pivot:
            l += 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if s <= k <= r:
        return quick_select(nums, s, r, k)
    elif l <= k <= e:
        return quick_select(nums, l, e, k)
    else:
        return nums[k]


'''
Union by rank with path compression O()
O(m log* n), amortized to be O(log*n), where m is number of operations, n is number of elements
'''


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x):
        # path compression
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True
