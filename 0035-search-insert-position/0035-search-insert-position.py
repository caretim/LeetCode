class Solution(object):
    def searchInsert(self, nums, target):
        left =0
        right = len(nums)-1
        now = 0
        while left<=right:
            mid = (left+right)//2
            m = nums[mid]
            if nums[mid]== target:
                return mid
            if nums[mid]>target:
                right=mid-1
            else:
                now =mid+1
                left=mid+1
        return now

