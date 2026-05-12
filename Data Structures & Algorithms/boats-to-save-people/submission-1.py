class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:
            remaining = limit - people[r]
            boats += 1
            r -= 1
            if people[l] <= remaining:
                l += 1

        return boats


# [5,4,2,1]
# [1,2,2,3,3]