class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashMap1 = {}
        hashMap2 = {}
        candidates = []

        for i in range(1, n + 1):
            hashMap1[i] = []
        for i in range(1, n + 1):
            hashMap2[i] = []

        for t in trust:
            hashMap1[t[0]].append(t[1])
            hashMap2[t[1]].append(t[0])

        for t in hashMap1:
            if not hashMap1[t]:
                candidates.append(t)
        
        for candidate in candidates:
            if len(hashMap2[candidate]) == n - 1:
                return candidate
        
        
        return -1

        print(hashMap1)
        print(hashMap2)

        
            

            