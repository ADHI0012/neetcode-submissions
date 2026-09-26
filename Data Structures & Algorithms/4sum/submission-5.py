class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            a = nums[i]
            if i > 0 and nums[i - 1] == a:
                continue
            
            three_sum = target - a

            for j in range(i + 1, n):
                b = nums[j]
                if j > i + 1 and b == nums[j - 1]:
                    continue
                two_sum = three_sum - b

                l,r = j + 1, n - 1

                while l < r:
                    t = nums[l] + nums[r]
                    if t == two_sum:
                        res.append([a,b,nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < n and nums[l] == nums[l - 1]:
                            l += 1
                        while r > 0 and nums[r] == nums[r + 1]:
                            r -= 1
                    elif t > two_sum:
                        r -= 1
                    else:
                        l += 1
        return res

