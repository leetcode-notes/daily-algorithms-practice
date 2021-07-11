from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:

        graph = defaultdict(set)

        for bus_number, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus_number)

        q = deque()
        q.append((source, 0))
        visited_stops = set()
        buses_taken = set()
        while q:
            cur_stop, count = q.popleft()
            if cur_stop == target:
                return count
            for next_bus in graph[cur_stop]:
                if next_bus not in buses_taken:
                    buses_taken.add(next_bus)
                    for next_stop in routes[next_bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append((next_stop, count+1))
        return -1


"""
Success
Details 
Runtime: 844 ms, faster than 20.73% of Python3 online submissions for Bus Routes.
Memory Usage: 50.2 MB, less than 23.92% of Python3 online submissions for Bus Routes.
Next challenges:
Kill Process
Flip Columns For Maximum Number of Equal Rows
Frog Position After T Seconds
"""
