class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                
                if count < 0:
                    return False
                    
            return count == 0

        res = []
    

        def dfs(i, curr, open, close):
            if open < close or open > n or close > n:
                return
            if i == 2*n:
                res.append("".join(curr))
                return
           
            
            curr.append("(")
            dfs(len(curr), curr, open + 1, close)
            curr.pop()
            curr.append(")")
            dfs(len(curr) , curr, open, close + 1)
            curr.pop()
            
        
        dfs(0,[],0,0)
    
    
        return res


        