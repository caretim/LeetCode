class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        dict ={}
        for i in magazine:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        
        for i in ransomNote:
            if i not in dict or dict[i]==0:
                return False
            dict[i]-=1
        
        return True

