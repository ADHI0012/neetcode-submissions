class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        curr_pow = 31

        while n:
            curr_bit = n % 2
            if curr_bit:
                res += 2**curr_pow
            curr_pow -= 1
            n = n >> 1

        return res

