class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1 > n2: return False

        map1 = {}
        map2 = {}

        for i in range(n1):
            map1[s1[i]] = 1 + map1.get(s1[i], 0)
            map2[s2[i]] = 1 + map2.get(s2[i], 0)
        
        if map1 == map2: return True

        for i in range(n2 - n1):
            outgoing_ch = s2[i]
            incoming_ch = s2[i + n1]
            map2[outgoing_ch] -= 1
            if map2[outgoing_ch] == 0:
                del map2[outgoing_ch]
            map2[incoming_ch] = 1 + map2.get(incoming_ch, 0)
            if map1 == map2:
                return True
        
        return False