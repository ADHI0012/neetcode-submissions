class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        
        freq = {}
        for num in hand:
            freq[num] = 1 + freq.get(num, 0)
        hand.sort()

        for n in hand:
            if freq[n] == 0:
                continue
            for i in range(n, n + groupSize):
            
                if i not in freq or freq[i] == 0:
                    return False
                freq[i] -= 1

        return True
        
      
                
        

       