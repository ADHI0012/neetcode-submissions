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
    

        def dfs(i, curr):
            if i == 2*n:
                if isValid(curr):
                    res.append(curr[:])
                return
            
            curr.append("(")
            dfs(len(curr), curr)
            curr.pop()
            curr.append(")")
            dfs(len(curr) , curr)
            curr.pop()
            
        
        dfs(0,[])
    
        finalRes = []
        for i in res:
            s = ""
            if i:
                for j in i:
                    s += j
            if s:
                finalRes.append(s)
    
        return finalRes


        