"""
# Definition for a Node.
# class Node(object):
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return 
        q = deque()
        visit = dict()
        visit[node.val]= Node(val=node.val)
        q.append(node)
        while q:
            cur=q.popleft()
            for i in cur.neighbors:
                if i.val not in visit:
                    visit[i.val]=Node(i.val)
                    q.append(i)
                visit[cur.val].neighbors.append(visit[i.val])

        return visit[node.val]



        """
        :type node: Node
        :rtype: Node
        """
        