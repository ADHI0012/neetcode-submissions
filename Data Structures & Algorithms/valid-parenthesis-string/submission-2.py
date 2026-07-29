class Solution:
    def checkValidString(self, s: str) -> bool:
        stackOpen = []
        stackStar = []

        for i in range(len(s)):
            if s[i] == "(":
                stackOpen.append(i)
            elif s[i] == "*":
                stackStar.append(i)
            else:
                if len(stackOpen) == 0:
                    if len(stackStar) == 0:
                        return False
                    else:
                        stackStar.pop()
                else:
                    stackOpen.pop()

        while stackOpen and stackStar:
            if stackOpen[-1] > stackStar[-1]:
                return False
            stackOpen.pop()
            stackStar.pop()

        return len(stackOpen) == 0
