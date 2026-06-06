class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        string_to_num = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        num_to_string = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

        def build_num(string):
            num = 0
            for i in range(len(string)):
                num = num * 10 + string_to_num[string[i]]
            return num
        def build_string(num):
            if num == 0:
                return "0"
            string = ""
            while num:
                string += num_to_string[num % 10]
                num = num // 10
            return string[::-1]

        num1 = build_num(num1)
        num2 = build_num(num2)

        return build_string(num1 * num2)