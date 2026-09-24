class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def dfs(i, xor):
            nonlocal total
            if i == len(nums):
                total += xor
                return
            
            dfs(i + 1, xor ^ nums[i])
            dfs(i + 1, xor)
        
        dfs(0,0)
        return total
