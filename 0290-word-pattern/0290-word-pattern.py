class Solution(object):
    def wordPattern(self, pattern, s):
        dict1 ={}
        dict2 ={}
        ls= list((s.split(' ')))
        if len(pattern) != len(ls):
            return False
        for p,w in zip(pattern,ls):
            if p not in dict1 and w not in dict2:
                dict1[p] = w
                dict2[w] = p
            elif p in dict1 and w in dict2:
                if dict1[p] != w or dict2[w] != p:
                    return False
            else:
                return False
        return True 
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """