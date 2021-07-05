"""
Ejenta is throwing a party! But we have to first figure out whom to invite. We have N people to choose from and we also have a list of which pairs of people know each other. Assume that if person A knows person B, then person B also knows person A. We would like to invite as many people as possible subject to the following constraint: each person at the party needs to know at least five people that are also attending the party.


Implement an algorithm that takes a list of people and a list of pairs of people that know each other. The goal is to output the list of people that we should invite to the party. 


You can represent this information any way you want, but we will be evaluating the code for both correctness and style. For this problem you should emphasize style and maintainability over efficiency.


You may use whatever programming language you like.



P.S. Test cases are not required but a non-trivial test could help you think through the problem carefully.
"""
from collections import Counter, defaultdict


def dfs(node, graph, connections=0):
    if not node:
        return connections
    for nei in graph[node]:
        dfs(nei, graph, connections+1)


def get_invitees(connections, people):
    graph = defaultdict(list)
    degrees = Counter()
    to_invite = []
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    for person in people:
        num_connections = dfs(person, graph, 0)
        if num_connections >= 5:
            to_invite.append(person)
    return to_invite


"""
   a 
b     c   d  


"""
