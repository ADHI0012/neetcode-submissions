class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        s = set("0123456789")
        total = 0

        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False


        for op in operations:
            if is_int(op):
                record.append(int(op))
            elif op == "+":
                if record:
                    sc1 = record[-1]
                    sc2 = record[-2]
                    record.append(sc1 + sc2)
            elif op == "C":
                record.pop()
            elif op == "D":
                sc = record[-1]
                record.append(sc * 2)
        
        for score in record:
            total += score

        return total
