class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 逆波兰表达式
        # tokens = ["4", "13", "5", "/", "+"] == 4 + (13 / 5) = 6
        # 遇到数字先存起来，遇到操作符就处理最近存进去的数字。
        stack = []

        for t in tokens:
            if t in "+-*/":
                # 把左右操作数都pop出来
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a /b))

            else:
                stack.append(int(t))
        return stack[0]