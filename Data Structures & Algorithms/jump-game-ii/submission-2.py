class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        jumps = 0
        def get_farthest(l,r):
            farthest = float('-inf')
            jump_index = -1
            for i in range(l + 1 ,r + 1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]
                    jump_index = i

            return [jump_index, farthest]

        distance = i = jumps = 0
        while i < n - 1:
            j = i + nums[i]
            if j >= n - 1:
                return jumps + 1
            i, distance = get_farthest(i,j)
            jumps += 1

        return jumps
        

        