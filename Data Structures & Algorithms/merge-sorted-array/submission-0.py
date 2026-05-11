class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []
        l = 0
        r = 0

        while l != m and r != n:
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        for i in range(l, m):
            res.append(nums1[i])
        for i in range(r, n):
            res.append(nums2[i])


        for i in range(len(nums1)):
            nums1[i] = res[i]