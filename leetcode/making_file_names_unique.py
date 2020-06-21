class Solution:
    def getFolderNames(self, names):
        d = {}
        res = []
        for name in names:
            if name not in d:
                res.append(name)
                d[name] = 1
            else:
                new_name = name+"({})".format(d[name])
                while new_name in d:
                    d[name] += 1
                    d[new_name] = 1
                    new_name = name+"({})".format(d[name])
                new_name = name+"({})".format(d[name])
                d[new_name] = 1
                d[name] += 1
                res.append(new_name)
        return res


'''
Input:
["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
Output:
["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)"]
Expected:
["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]
'''

# t5 = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
t5 = ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]
s = Solution()
print(s.getFolderNames(t5))
