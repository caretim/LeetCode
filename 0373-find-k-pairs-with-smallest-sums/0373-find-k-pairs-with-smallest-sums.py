import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return
        heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(heap)<k:
                    heapq.heappush(heap,(-(nums1[i]+ nums2[j]),[nums1[i],nums2[j]]))
                else:
                    if heap[0][0] < -(nums1[i] + nums2[j]):
                        heapq.heappop(heap)
                        heapq.heappush(heap,(-(nums1[i]+ nums2[j]),[nums1[i],nums2[j]]))
                    else:
                        break
        return [i[1] for i in heap]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        