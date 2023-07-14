from lexico import tokens
import ply.yacc as yacc
#Xavier Magallanes
def p_program(p):
    '''program : program item
                | item'''

def p_item(p):
    '''item : definicion
            | estructuracontrol
            | PRINT EXCLAMATION LPAREN STRING RPAREN SEMICOLON
            | PRINT EXCLAMATION LPAREN STRING COMMA expresion RPAREN SEMICOLON
            | PRINT EXCLAMATION LPAREN STRING COMMA vars  RPAREN SEMICOLON
            | expresion
            | expresion SEMICOLON
            | continue
            | break
            | funcionesesdata
            | RETURN expresion SEMICOLON
            | import
            | llamadarandom
            '''

def p_estructuracontrol(p):
    '''estructuracontrol : for
                        | while
                        | if
                        | loop'''


def p_for(p):
    '''for : FOR VARIABLE IN VARIABLE LBRACKET program RBRACKET
            | FOR VARIABLE IN VARIABLE LBRACKET RBRACKET
            | FOR VARIABLE IN NUMBER DOT DOT EQUAL NUMBER LBRACKET program RBRACKET
            | FOR VARIABLE IN NUMBER DOT DOT EQUAL NUMBER LBRACKET RBRACKET
            | FOR VARIABLE IN expresion LBRACKET program RBRACKET
            | FOR VARIABLE IN expresion LBRACKET RBRACKET'''

def p_definicion(p):
    '''definicion : definicionvariable
                    | definicionestructura
                    | definicionfuncion
                    | definicionestructuradatos'''
    

def p_definicionestructuradatos(p):
    '''definicionestructuradatos : hashmap
                                | array
                                | vector
                                | list'''
    
def p_list(p):
    ''' list : LET VARIABLE EQUAL L_BRACKET numeros R_BRACKET SEMICOLON'''

def p_numeros(p):
    ''' numeros : NUMBER
                | NUMBER COMMA numeros'''

def p_hashmap(p):
    '''hashmap : LET MUT VARIABLE DOUBLE_POINT HASHMAP LDIAMOND tipo COMMA tipo RDIAMOND EQUAL HASHMAP DOUBLE_POINT DOUBLE_POINT NEW LPAREN RPAREN SEMICOLON'''

def p_funcioneshashmap(p):
    ''' funcioneshashmap : VARIABLE DOT INSERT LPAREN expresion COMMA expresion RPAREN 
                            | VARIABLE DOT REMOVE LPAREN expresion RPAREN 
                            | VARIABLE DOT GET LPAREN expresion RPAREN 
                            | VARIABLE DOT LEN LPAREN RPAREN 
                            | VARIABLE DOT IS_EMPTY LPAREN RPAREN 
                            | VARIABLE DOT CLEAR LPAREN RPAREN 
                            | VARIABLE DOT ITER LPAREN RPAREN '''

def p_definicionestructura(p):
    '''definicionestructura : STRUCT VARIABLE LBRACKET item RBRACKET SEMICOLON
                            | STRUCT VARIABLE LBRACKET RBRACKET SEMICOLON'''

def p_definicionvariable(p):
    '''definicionvariable : LET VARIABLE DOUBLE_POINT tipo EQUAL expresion SEMICOLON
                            | LET VARIABLE EQUAL expresion SEMICOLON
                            | LET MUT VARIABLE EQUAL expresion SEMICOLON
                            | LET MUT VARIABLE DOUBLE_POINT tipo EQUAL expresion SEMICOLON
                            | LET VARIABLE DOUBLE_POINT tipo EQUAL STRING SEMICOLON
                            | LET MUT VARIABLE DOUBLE_POINT tipo EQUAL STRING SEMICOLON
                            | LET VARIABLE DOUBLE_POINT tipo SEMICOLON
                            | LET MUT VARIABLE DOUBLE_POINT tipo SEMICOLON
                            | LET VARIABLE SEMICOLON
                            | VARIABLE EQUAL expresion SEMICOLON
                            | VARIABLE EQUAL STRING SEMICOLON
                            | LET VARIABLE EQUAL expresion
                            | declaracion_constante
                            | declaracion_mutable
                            | LET VARIABLE LPAREN VARIABLE RPAREN EQUAL llamarfuncion
                            | LET MUT VARIABLE EQUAL llamadarandom'''
    
def p_vars(p):
    '''vars : VARIABLE
            | VARIABLE COMMA vars'''

def p_tipo(p):
    '''tipo : INT8
            | INT16
            | INT32
            | INT64
            | UINT8
            | UINT16
            | UINT32
            | UINT64
            | FLOAT32
            | FLOAT64
            | BOOL
            | CHAR
            | STR
            | VARIABLE
            | VEC tipo '''

def p_expresion(p):
    '''expresion : ops
                | NUMBER
                | FLOAT
                | STRING
                | TRUE
                | FALSE
                | VARIABLE
                | expresion
                | opbasicas
                | estructuracontrol
                | definicionvariable
                | llamarfuncion'''

def p_llamarfuncion(p):
    '''llamarfuncion : VARIABLE LPAREN RPAREN SEMICOLON
                    | VARIABLE LPAREN expresion RPAREN SEMICOLON
                    | VARIABLE LPAREN expresion COMMA expresion RPAREN SEMICOLON
                    | VARIABLE LPAREN operandos RPAREN SEMICOLON 
                    | VARIABLE LPAREN operandos RPAREN '''
    
def p_operaciones(p):
    ''' operaciones : PLUS
            | MINUS
            | TIMES
            | DIVIDE
            | RDIAMOND
            | LDIAMOND
            | EQUAL_EQUAL
            | NOT_EQUAL
            | LESS_EQUAL
            | GREATER_EQUAL
            | PLUS_EQUAL'''
    
def p_operandos(p):
    '''operandos : NUMBER
                | FLOAT
                | VARIABLE 
                | STRING
                | opbasicas
                | TIMES VARIABLE
                | BITAND VARIABLE
                | operandos COMMA operandos'''
    
def p_variables(p):
    '''variables : VARIABLE
                | VARIABLE COMMA variables'''



def p_definicionfuncion(p):
    '''definicionfuncion : funciongenerica

'''

def p_funciongenerica(p):
    '''funciongenerica : FN VARIABLE LPAREN RPAREN LBRACKET program RBRACKET
                        | FN MAIN LPAREN RPAREN LBRACKET program RBRACKET'''


#FAUSTO JACOME
def p_array(p):
    ''' array : LET MUT ARRAY DOUBLE_POINT L_BRACKET tipo SEMICOLON NUMBER R_BRACKET EQUAL L_BRACKET NUMBER SEMICOLON NUMBER R_BRACKET SEMICOLON
        | LET MUT VARIABLE DOUBLE_POINT array SEMICOLON'''
def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN LBRACKET program RBRACKET
            | WHILE  expresion LBRACKET program RBRACKET'''


def p_funcionesarray(p):
    ''' funcionesarray : VARIABLE DOT LEN LPAREN RPAREN SEMICOLON
                        | VARIABLE DOT IS_EMPTY LPAREN RPAREN SEMICOLON
                        | VARIABLE DOT CLEAR LPAREN RPAREN SEMICOLON
                        | VARIABLE DOT ITER LPAREN RPAREN SEMICOLON'''

def p_import(p):
    ''' import : USE VARIABLE DOUBLE_POINT DOUBLE_POINT VARIABLE SEMICOLON'''
def p_llamadarandom(p):
    ''' llamadarandom : VARIABLE DOUBLE_POINT DOUBLE_POINT VARIABLE LPAREN RPAREN SEMICOLON'''


#ALEJANDRO DONOSO

def p_expresionlogica(p):
    '''expresionlogica : operandos AND operandos
                        | operandos OR operandos
                        | operandos
                        | TRUE
                        | FALSE'''
    
def p_break(p):
    '''break : BREAK SEMICOLON
            | BREAK expresion SEMICOLON'''
def p_continue(p):
    '''continue : CONTINUE SEMICOLON'''

def p_declaracion_constante(p):
    '''declaracion_constante : CONST VARIABLE DOUBLE_POINT tipo EQUAL expresion SEMICOLON
                             | CONST VARIABLE DOUBLE_POINT tipo SEMICOLON
                             | CONST VARIABLE EQUAL expresion SEMICOLON
                             | CONST VARIABLE SEMICOLON'''
def p_declaracion_mutable(p):
    '''declaracion_mutable : MUT VARIABLE DOUBLE_POINT tipo EQUAL expresion SEMICOLON
                           | MUT VARIABLE DOUBLE_POINT tipo SEMICOLON
                           | MUT VARIABLE EQUAL expresion SEMICOLON
                           | MUT VARIABLE SEMICOLON'''

def p_if(p):
    ''' if : IF expresion LBRACKET program RBRACKET 
           | IF expresion LBRACKET program RBRACKET ELSE 
           | IF expresion LBRACKET program RBRACKET ELSE LBRACKET program RBRACKET'''
    
def p_loop(p):
    '''loop : LOOP LBRACKET program RBRACKET'''

def p_vector(p):
    '''vector : LET VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND EQUAL expresion SEMICOLON
                          | LET VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND SEMICOLON
                          | LET  MUT VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND EQUAL expresion SEMICOLON
                          | LET MUT VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND SEMICOLON
                          | LET VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND EQUAL VEC DOUBLE_POINT DOUBLE_POINT NEW LPAREN RPAREN SEMICOLON '''
def p_funcionesesdata(p):
    '''funcionesesdata : funcionesvector
                        | funcioneshashmap
                        | funcionesarray'''

def p_funcionesvector(p):
    ''' funcionesvector : VARIABLE DOT PUSH LPAREN expresion RPAREN SEMICOLON
                         | VARIABLE DOT POP LPAREN RPAREN SEMICOLON
                         | VARIABLE DOT LEN LPAREN RPAREN SEMICOLON
                         | VARIABLE DOT IS_EMPTY LPAREN RPAREN SEMICOLON
                         | VARIABLE DOT GET LPAREN NUMBER RPAREN SEMICOLON
                         | VARIABLE DOT SET LPAREN NUMBER COMMA expresion RPAREN SEMICOLON
                         | VARIABLE DOT REMOVE LPAREN expresion RPAREN SEMICOLON
                         | VARIABLE DOT CLEAR LPAREN RPAREN SEMICOLON
                         | VARIABLE DOT SWAP LPAREN expresion COMMA expresion RPAREN SEMICOLON
                         | VARIABLE DOT REVERSE LPAREN RPAREN SEMICOLON
                         | VARIABLE DOT ITER LPAREN RPAREN SEMICOLON'''
def p_opbasicas(p):
    '''opbasicas : ARRAY DOT LEN LPAREN RPAREN
                   | BITAND VARIABLE L_BRACKET NUMBER DOT DOT NUMBER R_BRACKET
                   | VARIABLE DOT ITER LPAREN RPAREN
                    | ARRAY L_BRACKET operandos R_BRACKET
                   | LPAREN NUMBER DOT DOT NUMBER RPAREN DOT REV LPAREN RPAREN
                   | STRING DOT TO_STRING LPAREN RPAREN
                   | VARIABLE LPAREN variables RPAREN
                   | VEC EXCLAMATION L_BRACKET numeros R_BRACKET
                   | VARIABLE DOT VARIABLE LPAREN RPAREN 
                   '''




def p_ops(p):
        ''' ops : operandos operaciones operandos
            | operandos operaciones ops '''

def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
    else:
         print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()
