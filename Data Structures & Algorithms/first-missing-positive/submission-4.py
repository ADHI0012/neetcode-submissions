class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_positive = float('inf')

        for num in nums:
            if num >= 0:
                if num < min_positive:
                    min_positive = num

        if min_positive == float('inf'):
            return 1

        i = 1

        for j in range(1, int(min_positive)):
            if j not in nums:
                return j

        while True:
            if min_positive + i not in nums:
                return min_positive + i
            i += 1
       
        

            
