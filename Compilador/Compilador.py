from Lex import *
from TokenType import *

def main():
   # input = "IF+-123123 algo*THEN"

    file = open("./code.mchess","r")
    input = file.read()

    lexer = Lexer(input)
    token = lexer.getToken()

    cont = 0

    while token.kind != TokenType.EOF:
        print("Token Type: {} , Content: {}".format(token.kind, token.text))
        token = lexer.getToken()
        cont+=1
    print("Number tokens found: {}".format(cont))

main()
