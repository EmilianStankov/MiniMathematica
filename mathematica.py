from rpn import RPN
import math


class MiniMathematica:
    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '^': lambda a, b: a ** b,
            'pow': lambda a, b: a ** b,
            'sqrt': lambda a: a ** (1/2),
            'nthrt': lambda a, b: a ** (1/b),
            'log': lambda a, b: math.log(b, a),
            'sin': lambda a: math.sin(a),
            'cos': lambda a: math.cos(a),
            'tg': lambda a: math.tan(a),
            'cotg': lambda a: 1/math.tan(a)
        }
        self.single_argument_operators = ['sqrt', 'sin', 'cos', 'tg', 'cotg']
        self.constants = {
            'pi': 3.14159265359,
            'PI': 3.14159265359,
            'Pi': 3.14159265359,
            'e': 2.71828182846,
            'E': 2.71828182846
        }

    def calculate(self, expression):
        rpn = RPN(expression).to_reverse_polish()
        stack = []
        while rpn:
            token = rpn.pop(0)
            if token == '-' and len(stack) < 2:
                a = stack.pop()
                stack.append(-float(a))
            elif token in self.operators:
                if token in self.single_argument_operators:
                    a = stack.pop()
                    stack.append(self.operators[token](a))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self.operators[token](a, b))
            else:
                if token in self.constants:
                    stack.append(self.constants[token])
                else:
                    stack.append(float(token))
        return stack[0]
