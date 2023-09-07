# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def kthSmallest(self, root, k):
        self.cnt = k
        self.result = None
        self.find(root)
        return self.result
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    def find(self,node):
        if node is None:
            return             
        self.find(node.left)
        self.cnt-=1
        if self.cnt == 0:
            self.result = node.val
            return 
        self.find(node.right)
        