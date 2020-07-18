from collections import defaultdict


class Solution:
    def sortItems(self, n: int, m: int, group, beforeItems):

        # rearrange group[i:[item1, item2 ...]]
        group_to_item = defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group_to_item[group[i]].add(i)
        item_pred, item_succ = defaultdict(set), defaultdict(set)
        group_pred, group_succ = defaultdict(set), defaultdict(set)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    item_pred[i].add(j)
                    item_succ[j].add(i)
                else:
                    group_pred[group[i]].add(group[j])
                    group_succ[group[j]].add(group[i])

        sorted_groups = self.topSort(
            list(group_to_item.keys()), group_pred, group_succ)
        sorted_items = []
        for g in sorted_groups:
            items = self.topSort(group_to_item[g], item_pred, item_succ)
            if len(items) != len(group_to_item[g]):
                return []
            sorted_items.extend(items)
        return sorted_items if len(sorted_items) == n else []

    def topSort(self, node_list, pred, succ):
        res = []
        sources = [n for n in node_list if not pred[n]]
        while sources:
            s = sources.pop()
            res.append(s)
            for u in succ[s]:
                pred[u].remove(s)
                if not pred[u]:
                    sources.append(u)
        return res if len(res) == len(node_list) else []


'''
Success
Details
Runtime: 528 ms, faster than 75.58% of Python3
Memory Usage: 55 MB, less than 11.43% of Python3
Next challenges:
Convert Sorted Array to Binary Search Tree
Reconstruct Itinerary
Network Delay Time
'''
