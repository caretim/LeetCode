class Solution(object):
    def averageOfLevels(self, root):
        self.depth = 0
        self.result=[]
        self.count =[]
        self.find(root,0)
        print(self.result,self.count)
        for i in range(len(self.result)):
            self.result[i]= float(self.result[i])/float(self.count[i])
    
        return self.result
            
    def find(self,node,depth):
        if node== None:
            return
        if len(self.result)==depth:
            self.result.append(node.val)
            self.count.append(1)
        else:
            self.result[depth]+=node.val
            self.count[depth]+=1
        self.find(node.left,depth+1)
        self.find(node.right,depth+1)