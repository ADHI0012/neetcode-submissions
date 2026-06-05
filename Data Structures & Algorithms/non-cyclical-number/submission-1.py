class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num = num // 10
            return total

        seen = set()

        while True:
            n = get_sum(n)
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)

        