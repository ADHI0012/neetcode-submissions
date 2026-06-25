class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        freq = dict(sorted(freq.items(), key=lambda item: (item[1], -item[0])))

        for num in freq:
            for _ in range(freq[num]):
                res.append(num)

        return res



        

# sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
