from lexer import Token
from ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = lexer.next_token()

    def eat(self, type_):
        if self.current.type == type_:
            self.current = self.lexer.next_token()
        else:
            raise Exception(f'Unexpected token: {self.current.type}')

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()
        while self.current.type == Token.OR:
            self.eat(Token.OR)
            node = OrNode(node, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current.type in (Token.CHAR, Token.LPAREN):
            node = ConcatNode(node, self.factor())
        return node

    def factor(self):
        node = None
        if self.current.type == Token.CHAR:
            node = CharNode(self.current.value)
            self.eat(Token.CHAR)
        elif self.current.type == Token.LPAREN:
            self.eat(Token.LPAREN)
            node = self.expr()
            self.eat(Token.RPAREN)
        if self.current.type == Token.STAR:
            self.eat(Token.STAR)
            node = StarNode(node)
        return node
