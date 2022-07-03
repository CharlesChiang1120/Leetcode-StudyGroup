class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            i = len(nums1) // 2 -1
            return (nums1[i]+ nums1[i+1])/2
            
        else:
            i = len(nums1) // 2
            return nums1[i]
