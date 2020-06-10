'''
You are given a tree that contains N nodes, each containing an integer u which
 corresponds to a lowercase character c in the string s using 1-based indexing

You are required to answer Q queries of type [u, c] where u is an integer and
 c is a lowercase letter.
 s = "aba"
rootnode = 1
query = [[1, 'a']]
output = 2
'''
from collections import deque
from typing import Dict


class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

def resolveQueries(queries, string, root):
    queryDict = {}
    # store the queries with node as key
    for query in queries:
        node, char = query[0], query[1]
        queryDict[node] = char 
    # traverse the tree, whenever a node is in queryDict, run "solve"
    queue = deque([])
    queue.append(root)
    lookup = generate_lookup(string)
    res = {}
    while queue:
        qlength = len(queue)
        for i in range(qlength):
            curNode = queue.popleft()
            if curNode in queryDict:
                count = solve(curNode, queryDict[curNode], lookup)
                # store the result of solve
                res[curNode.val] = count 
                # remove after we have called solve
                del queryDict[curNode]
    return res 


def generate_lookup(string):
    int_to_char = {}
    for i in range(len(s)):
        int_to_char[i+1] = s[i]
    return int_to_char


def solve(startNode, char, lookup: Dict) -> int:
    queue = deque([])
    queue.append(startNode)
    count = 0
    while queue:
        qlength = len(queue)
        for i in range(qlength):
            cur_node = queue.popleft()
            if lookup[cur_node.val] == char:
                count += 1
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return count


# test 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
query = [[1, 'a']]
s = "aba"

lookup = generate_lookup(s)
print(lookup)
query = [1, 'a']
print(solve(root, 'a', lookup))
