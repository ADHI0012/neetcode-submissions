class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array = []
        n,m = len(nums1), len(nums2)
        l,r = 0,0

        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                new_array.append(nums1[l])
                l += 1
            else:
                new_array.append(nums2[r])
                r += 1

        while l < n:
            new_array.append(nums1[l])
            l += 1
        while r < m:
            new_array.append(nums2[r])
            r += 1

        N = len(new_array)

        if N % 2:
            return new_array[(N // 2)]

        a = N // 2
        b = (N // 2) - 1

        return (new_array[a] + new_array[b]) / 2


        