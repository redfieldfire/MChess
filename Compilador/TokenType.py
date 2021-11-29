#definir todos los tokens enumerlos
import enum
class TokenType(enum.Enum):
    
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    ##KEYWORD

    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    #Actions
    Move = 115
    Capture = 116
    Castling = 117

    #Pieces
    Queen = 120
    King = 121
    Bishop = 122
    Knight = 123
    Pawn = 124
    Rook = 125

    #Directions
    To = 130

    #Boxes
    Box = 140

    #Types
    Short = 150
    Long = 151

    #Effects
    Check = 160
    CheckMate = 161

    #Auxiliaries
    With = 170
    And = 171

    ##OPERADORES

    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    



