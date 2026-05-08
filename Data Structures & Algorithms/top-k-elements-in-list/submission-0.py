class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hashMap = {}
        maxOcc = 0
        resultArray = []
        for i in range(n):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
            maxOcc = max(maxOcc, hashMap[nums[i]])
        hashMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))

        print(hashMap)

        for i in hashMap:
            if (len(resultArray) == k):
                break
            resultArray.append(i)

        return resultArray