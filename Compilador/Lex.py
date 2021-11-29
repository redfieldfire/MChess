import sys
import re
from Token import Token
from TokenType import *

class Lexer:

    #contructor
    def __init__(self,input):
        self.source =  input
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    #procesa el caracter actual
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = "\0" #EOF
        else:
            self.curChar = self.source[self.curPos]

    #anticipa el caracter que sigue
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    #muestra el error por si hay token invalido
    def abort(self, message):
        sys.exit("Error de lexico" + message)

    #skip los espacios en blanco
    def skipWhiteSpace (self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    #skip comentarios
    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

    #obtiene el token siguiente
    def getToken(self):
        self.skipWhiteSpace()
        self.skipComment()
        token = None
        #checkar si el primer caracter + =
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '=':

            #Verificar si estan asignando o comparando
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        #Mayor que
        elif self.curChar == '>':

            #Verificar si comparando mayor
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)

        #Menor que
        elif self.curChar == '<':

            #Verificar si comparando
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)

        #Diferente que
        elif self.curChar == '!':

            #Verificar si comparando
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Se esperaba un != y escribiste !" + self.peek())

        #Verificando los textos multilineas
        elif self.curChar == '\"':
            self.nextChar()
            startPosition = self.curPos
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Caracter no valido en el String")
                self.nextChar()

            tokenText = self.source[startPosition:self.curPos]
            token = Token(tokenText , TokenType.STRING)

        elif self.curChar.isdigit():
            startPosition = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Caracter no valido en el numero")
                
                while self.peek().isdigit():
                    self.nextChar()

            tokenText = self.source[startPosition: self.curPos + 1]
            token = Token(tokenText,TokenType.NUMBER)

        elif self.curChar.isalpha():
            startPosition = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokenText = self.source[startPosition: self.curPos + 1]
            keyWord = Token.checkIfKeyword(tokenText)

            if keyWord == None:
                #Coordenada
                expresion = "[a-h][1-8]"
                if re.fullmatch(expresion,tokenText):
                    token = Token(tokenText, TokenType.Box)
            
            else:
                token = Token(tokenText, keyWord)

        elif self.curChar == '\n':
            token = Token(self.curChar,TokenType.NEWLINE)

        elif self.curChar == '\0':
            token = Token(self.curChar,TokenType.EOF)

        else:
            self.abort("Token desconocido " + self.curChar)

        self.nextChar()
        return token





