class Token:
    CHAR, STAR, OR, LPAREN, RPAREN, EOF = 'CHAR', 'STAR', 'OR', 'LPAREN', 'RPAREN', 'EOF'

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

class Lexer:
    def __init__(self, pattern):
        self.pattern = pattern
        self.pos = 0

    def next_token(self):
        if self.pos >= len(self.pattern):
            return Token(Token.EOF)
        c = self.pattern[self.pos]
        self.pos += 1
        if c == '*':
            return Token(Token.STAR)
        if c == '|':
            return Token(Token.OR)
        if c == '(':
            return Token(Token.LPAREN)
        if c == ')':
            return Token(Token.RPAREN)
        return Token(Token.CHAR, c)
