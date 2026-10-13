class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s):
            n = len(s)
            op = cl = 0
            for ch in s:
                if ch == "(":
                    op += 1
                else:
                    cl += 1
                if cl > op:
                    return False
            
            return True

        def dfs(i,curr, op, cl):
            if op > n or cl > n:
                return
            if op + cl == 2 * n:
                paran = "".join(curr)
                if isValid(paran):
                    res.append(paran)
                return
            
            curr.append("(")
            dfs(i + 1, curr, op + 1, cl)
            curr.pop()
            curr.append(")")
            dfs(i + 1, curr, op, cl + 1)
            curr.pop()
        
        dfs(0,[],0,0)
        return res

        