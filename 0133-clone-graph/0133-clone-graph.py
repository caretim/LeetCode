"""
Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                visited[node].neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)