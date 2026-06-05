class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                if digits[i] + 1 >= 10:
                    carry = 1
                    digits[i] = (digits[i] + 1) % 10
                else:
                    digits[i] += 1
            else:
                value = digits[i] + carry
                if value >= 10:
                    carry = 1
                    value = value % 10
                else:
                    carry = 0
                digits[i] = value 

        if carry:
            digits.insert(0,1)

        return digits
            