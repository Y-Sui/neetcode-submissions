class Solution:
    def calculate(self, s: str) -> int:
        # s expression, return the value
        # eval()
        # division should truncate towards zero, 5/2 = 2
        # priority issue: */ > +-
        # edge cases like blank sapce

        # solution:
        # we can safely push the number to stack when +/-
        # we compute the number with its previous number (top of stack) and push back when *//
       
        s = s.replace(" ", "")

        stack = []
        operator = "+"
        curr_num = 0

        for i, ch in enumerate(s):
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # Process the number when we hit an operator or reach the end of string
            if ch in '+-/*' or (i == len(s) -1) :
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    stack.append(stack.pop() * curr_num)
                else:
                    stack.append(int(stack.pop() / curr_num))

                operator = ch
                curr_num = 0

        return sum(stack)