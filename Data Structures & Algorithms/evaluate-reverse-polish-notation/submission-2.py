class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+' : 0, '-' : 1, '*' : 2, '/' : 3}

        def is_int(token):
            try:
                int(token)
                return True
            except ValueError:
                return False

        for token in tokens:
            if is_int(token):
                stack.append(token)
            elif token in operators:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if operators[token] == 0:
                    stack.append(op2 + op1)
                elif operators[token] == 1:
                    stack.append(op2 - op1)
                elif operators[token] == 2:
                    stack.append(op2 * op1)
                else:
                    stack.append(int(op2 / op1))

        return int(stack.pop())
