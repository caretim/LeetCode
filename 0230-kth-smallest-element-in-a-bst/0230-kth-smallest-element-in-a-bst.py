class Solution(object):
    def kthSmallest(self, root, k):
        self.result = []
        self.find(root)
        return self.result[k-1]
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    def find(self,node):
        if node is None:
            return             
        self.find(node.left)
        self.result.append(node.val)
        self.find(node.right)