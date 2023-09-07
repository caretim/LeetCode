class Solution(object):
    def rightSideView(self, root):
        self.result = []
        self.findRight(root,0)
        return self.result
    
    def findRight(self, node,level):
        if node == None:
            return
        if len(self.result) == level:
            self.result.append(node.val)
        self.findRight(node.right,level+1)
        self.findRight(node.left,level+1)