from lexico import tokens
import ply.yacc as yacc

# Xavier Magallanes
def p_programa(p):
    '''programa : programa item
                | item'''

def p_item(p):
    '''item : declaracion
            | importacion
            | funcion
            | error'''

def p_declaracion(p):
    '''declaracion : declaracion_variable
                     | declaracion_estructura'''
    
def p_declaracion_variable(p):
    '''declaracion_variable : LET VARIABLE DOUBLE_POINT tipo EQUAL expresion SEMICOLON
                            | LET VARIABLE DOUBLE_POINT tipo SEMICOLON
                            | LET VARIABLE EQUAL expresion SEMICOLON
                            | LET VARIABLE SEMICOLON'''


def p_declaracion_estructura(p):
    '''declaracion_estructura : STRUCT VARIABLE LBRACKET campos RBRACKET SEMICOLON
                              | STRUCT VARIABLE LBRACKET RBRACKET SEMICOLON'''


def p_campos(p):
    '''campos : campos COMMA campo
              | campo'''

def p_campo(p):
    '''campo : VARIABLE DOUBLE_POINT tipo'''

def p_tipo(p):
    '''tipo : tipo_simple '''

def p_tipo_simple(p):
    '''tipo_simple : INT8
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
                    | STR'''

def p_importacion(p):
    '''importacion : USE VARIABLE SEMICOLON'''

def p_funcion(p):
    '''funcion : funcion_generica'''

def p_funcion_generica(p):
    '''funcion_generica : FN VARIABLE LPAREN parametros RPAREN ARROW tipo_simple bloque'''


def p_parametros(p):
    '''parametros : parametros COMMA parametro
                  | parametro
                  | empty'''
    
def p_empty(p):
    'empty :'
    pass

def p_parametro(p):
    '''parametro : VARIABLE DOUBLE_POINT tipo'''

def p_bloque(p):
    '''bloque : LBRACKET sentencias RBRACKET'''

def p_sentencias(p):
    '''sentencias : sentencias sentencia
                  | sentencia'''

def p_sentencia(p):
    '''sentencia : expresion SEMICOLON
                 | declaracion
                 | asignacion'''

def p_asignacion(p):
    '''asignacion : VARIABLE EQUAL expresion SEMICOLON'''


def p_expresion(p):
    '''expresion : expresion_literal
                    | expresion_variable
                    | expresion_funcion
                    | expresion_estructura'''

def p_expresion_literal(p):
    '''expresion_literal : literal'''

def p_literal(p):
    '''literal : NUMBER
                | STRING
                | TRUE
                | FALSE'''
    
def p_expresion_variable(p):
    '''expresion_variable : VARIABLE'''

def p_expresion_funcion(p):
    '''expresion_funcion : VARIABLE LPAREN argumentos RPAREN SEMICOLON'''

def p_expresion_estructura(p):
    '''expresion_estructura : hashmap'''

def p_hashmap(p):
    '''hashmap : LDIAMOND hashmap_types RDIAMOND'''

def p_hashmap_types(p):
    '''hashmap_types : hashmap_types COMMA hashmap_type
                     | hashmap_type'''
    
def p_hashmap_type(p):
    '''hashmap_type : tipo'''


def p_argumentos(p):
    '''argumentos : argumentos COMMA argumento
                  | argumento
                  | empty'''

def p_argumento(p):
    '''argumento : expresion'''


    

def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

while True:
   try:
       s = input('rust > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)
