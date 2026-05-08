class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {[freq]: string}
        freq_map = defaultdict(list)
        for i in strs:
            count = [0 for _ in range(26)]
            for j in i:
                count[ord(j) - 97] += 1
            key = tuple(count)
            freq_map[key].append(i)

        return list(freq_map.values())