class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = twenty = 0
        for bill in bills:
            if bill == 5:
                fives += 1
                continue
            elif bill == 10:
                if fives == 0:
                    return False
                tens += 1
                fives -= 1
            else:
                if (fives == 0 or tens == 0) and fives < 3:
                    return False
                elif tens == 0 and fives > 3:
                    fives -= 3
                else:
                    tens -= 1
                    fives -= 1
                
        return True