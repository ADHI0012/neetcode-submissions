class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isMatching(open, close):
            return (
                open == "("
                and close == ")"
                or open == "["
                and close == "]"
                or open == "{"
                and close == "}"
            )

            
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")" or c == "}" or c == "]":
                if not stack:
                    return False
                res = isMatching(stack.pop(), c)
                if not res:
                    return False
            
        return len(stack) == 0
