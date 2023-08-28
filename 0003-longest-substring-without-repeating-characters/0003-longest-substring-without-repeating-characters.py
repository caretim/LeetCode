class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result =""
        max_length = 0
        for i in s:
            if i in result:
                result = result[result.index(i)+1:]
                """if abcdas is the string, here after abcd the length would be 4 and result will be replaced as bcda"""
            result += i
            max_length = max(max_length, len(result))
        return (max_length)
