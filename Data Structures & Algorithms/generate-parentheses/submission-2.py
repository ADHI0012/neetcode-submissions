class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
    

        def dfs(curr, open, close):
            if open < close or open > n or close > n:
                return
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
           
            
            curr.append("(")
            dfs(curr, open + 1, close)
            curr.pop()
            curr.append(")")
            dfs(curr, open, close + 1)
            curr.pop()
            
        
        dfs([],0,0)
    
    
        return res


        