from lexer import Lexer
from parser import Parser
from nfa import build_nfa
from matcher import match_nfa

def main():
    pattern = input("Enter regex: ")
    string = input("Enter string to match: ")
    lexer = Lexer(pattern)
    parser = Parser(lexer)
    ast = parser.parse()
    nfa = build_nfa(ast)
    result = match_nfa(nfa, string)
    print("Match!" if result else "No match.")

if __name__ == "__main__":
    main()
