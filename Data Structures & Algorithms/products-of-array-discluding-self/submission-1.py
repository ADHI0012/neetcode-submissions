class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pdt = 1
        result = []
        zero_count = 0
        for num in nums:
            if num != 0:
                pdt *= num
            else:
                zero_count += 1
        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if not num:
                    result.append(pdt)
                else:
                    result.append(0)
            else:
                result.append(int(pdt/num))

            

        return result