class Solution(object):
    def isAnagram(self, s, t):
        dict ={}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        
        for i in t:
            if i not in dict or dict[i]==0:
                return False
            dict[i]-=1
            
        for key,value in dict.items():
            if value >0:
                return False
        
        return True
