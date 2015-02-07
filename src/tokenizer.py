class Tokenizer:
    def __init__(self, operators):
        self.operators = operators

    def add_token(self, token, tokens):
        if token != '':
            tokens.append(token)

    def tokenize(self, expression):
        tokens = []
        current = ""
        for c in expression:
            current += c
            if c == ',':
                self.add_token(current[:-1], tokens)
                self.add_token(c, tokens)
                current = ""
            if current in self.operators:
                self.add_token(current, tokens)
                current = ""
                continue
            else:
                if c == " ":
                    self.add_token(current[:-1], tokens)
                    current = ""
                elif c in self.operators:
                    self.add_token(current[:-1], tokens)
                    self.add_token(c, tokens)
                    current = ""
        self.add_token(current, tokens)
        return tokens