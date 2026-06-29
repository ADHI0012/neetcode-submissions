class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = target[0], target[1], target[2]
        A = B = C = False

        for triplet in triplets:
            if triplet[0] > a or triplet[1] > b or triplet[2] > c:
                continue
            if triplet[0] == a: A = True
            if triplet[1] == b: B = True
            if triplet[2] == c: C = True

        if A and B and C: return True

        return False



