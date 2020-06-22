from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        if veganFriendly:
            c = [1]
        else:
            c = [0, 1]
        for r in restaurants:
            if not r[2] in c or r[4] > maxDistance or r[3] > maxPrice:
                continue
            else:
                res.append(r)
        res = sorted(res, key=lambda x: (x[1], x[0]), reverse=True)
        new_res = []
        for r in res:
            new_res.append(r[0])
        return new_res


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
    3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
v = 1
mp = 50
md = 10
s = Solution()
print(s.filterRestaurants(restaurants, v, mp, md))

'''
Success
Details 
Runtime: 360 ms, faster than 83.54% of Python3 online submissions for Filter Restaurants by Vegan-Friendly, Price and Distance.
Memory Usage: 22.6 MB, less than 30.49% of Python3 online submissions for Filter Restaurants by Vegan-Friendly, Price and Distance.
Next challenges:
Array Nesting
Available Captures for Rook
Largest Unique Number
'''
