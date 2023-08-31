class Solution(object):
    def isIsomorphic(self, s, t):
        dict1 ={}						
        dict2 ={}								
        if len(s) != len(t):		
            return False
        for p,w in zip(s,t):		
            if p not in dict1 and w not in dict2:  
                dict1[p] = w			
                dict2[w] = p
            elif p in dict1 and w in dict2:	
                if dict1[p] != w or dict2[w] != p: 
                    return False
            else:				
                return False			
        return True