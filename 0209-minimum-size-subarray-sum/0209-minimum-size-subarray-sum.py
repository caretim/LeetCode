class Solution(object):
    def minSubArrayLen(self,s, nums):
        min_range=1e9
        left =0
        temp = 0
        
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= s:
                min_range = min(min_range, i - left + 1)
                temp -= nums[left]
                left += 1
        if min_range == 1e9:
            min_range= 0

        return min_range