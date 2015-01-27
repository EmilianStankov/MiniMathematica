from tokenizer import Tokenizer
class RPN:
    def __init__(self, expression):
        self.operators = {
            '+': 1, '-': 1,
            '/': 2, '*': 2,
            '^': 3, 'sqrt': 3, 'nthrt': 3, 'pow': 3,
            'log': 4, 'sin': 4, 'cos': 4, 'tg': 4, 'cotg': 4,
            '(': 0, ')': 0
        }
        self.function_tokens = [
            'sqrt', 'nthrt', 'pow', 'log',
            'sin', 'cos', 'tg', 'cotg'
        ]
        self.association = {
            '+': "left",
            '-': "left",
            '*': "left",
            '/': "left",
            '^': "right",
        }
        self.expression = expression
        self.tokens = Tokenizer(self.operators).tokenize(expression)

    def to_reverse_polish(self):
        output = []
        ops = []
        for token in self.tokens:
            if self.is_function(token):
                ops.append(token)
            elif token == ',':
                while len(ops) > 0 and ops[-1] != '(':
                    output.append(ops.pop())
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while len(ops) > 0 and ops[-1] != '(':
                    output.append(ops.pop())
                if ops[-1] == '(':
                    ops.pop()
            elif self.is_operator(token):
                while len(ops) > 0 and \
                    ((self.association[token] == 'left' and \
                        self.operators[token] <= self.operators[ops[-1]]) \
                    or (self.association[token] == 'right' and \
                        self.operators[token] < self.operators[ops[-1]])):
                    output.append(ops.pop())
                ops.append(token)
            else:
                output.append(token)
        while len(ops) > 0:
            output.append(ops.pop())
        return output

    def is_operator(self, token):
        return token in self.operators and token not in [',', '(', ')']

    def is_function(self, token):
        return token in self.function_tokens
