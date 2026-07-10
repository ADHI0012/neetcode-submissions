class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def canBuild(gcd, string):
            count = 0
            s = ""
            for i in string:
                if s == gcd:
                    count += 1
                    s = ""
                s += i
            if s == gcd: count += 1

            return count == len(string) / len(gcd)

            

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        length = 0

        for i in range(1, len(str2) + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                length = i

        gcd = ""

        for i in range(length):
            gcd += str2[i]

        if canBuild(gcd, str1) and canBuild(gcd, str2):
            return gcd

        return ""

        
