"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color 
of the ith node in this graph (0-indexed). You are also given a 2D array edges where 
edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a 
directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of 
nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains 
a cycle.
"""

from typing import List, DefaultDict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        ### Mine, doesn't work
        # start = 0
        # cols = [colors[0]]
        
        # for edge in edges:
        #     if edge[1] <= edge[0]:
        #         return -1
        #     if edge[0] != start:
        #         start = edge[0]
        #         cols = [colors[0]]
            
        #     cols.append(colors[edge[1]])
        #     start = edge[1]

        # return cols.count(max(set(cols), key=cols.count))

        adj = DefaultDict(list)
        for x,y in edges:
            adj[x].append(y)

        def dfs(node):
            if node in path:
                return float("inf")
            if node in visited:
                return 0
            
            visited.add(node)
            path.add(node)

            ## count its color:
            colorInd = ord(colors[node]) - ord('a')
            count[node][colorInd] = 1

            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        (1 if c == colorInd else 0) + count[nei][c]
                    )
                
            path.remove(node)
            return max(count[node])


        n, res= len(colors), 0
        visited, path = set(), set()
        count = [[0] * 26 for i in range(n)]
        for i in range(n):
            res = max(dfs(i),res)
        return -1 if res == float('inf') else res
print(Solution().largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]]))