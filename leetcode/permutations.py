def dfs(nums, path, result):
    if (len(nums) == len(path)):
        result.append(path[:])
        return
    for n in nums:
        if n in path:
            continue
        path.append(n)
        dfs(nums, path, result)
        path.pop()


def permute(nums):
    res = []
    if not nums:
        return res
    dfs(nums, [], res)
    return res


print(permute([1, 2, 3]))
