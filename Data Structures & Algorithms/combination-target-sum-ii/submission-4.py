class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = set()
        candidates.sort()
        def dfs(i, total, arr):
            if total == target:
                seen.add(tuple(arr))
                return
            if i == len(candidates) or total > target:
                return
            arr.append(candidates[i])
            dfs(i + 1, total + candidates[i], arr)
            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total, arr)
        dfs(0,0,[])
        return [list(combination) for combination in seen]

