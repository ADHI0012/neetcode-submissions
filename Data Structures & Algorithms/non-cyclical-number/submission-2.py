class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num = num // 10
            return total

        slow, fast = n, get_sum(n)

        while slow != fast:
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))

        return fast == 1

        