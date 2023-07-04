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
                     | declaracion_estructura
                     | declaracion_constante
                     | declaracion_mutable
                     | declaracion_array 
                     | declaracion_struct_control
                     | declaracion_vector'''
    
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
                 | asignacion
                 | break
                 | funciones_vector
                 | funciones_hashmap'''



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
                | boolean'''

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    
def p_expresion_variable(p):
    '''expresion_variable : VARIABLE'''

def p_expresion_funcion(p):
    '''expresion_funcion : VARIABLE LPAREN argumentos RPAREN SEMICOLON'''

def p_expresion_estructura(p):
    '''expresion_estructura : hashmap
                | array 
                '''


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

#Fausto Jacome
def p_declaracion_array(p):
    ''' declaracion_array : LET MUT VARIABLE DOUBLE_POINT array EQUAL L_BRACKET array_fill R_BRACKET SEMICOLON
                | LET MUT VARIABLE DOUBLE_POINT array SEMICOLON '''
def p_array(p):
    ''' array : ARRAY L_BRACKET var_array R_BRACKET '''
    
def p_var_array(p):
    ''' var_array : tipo SEMICOLON NUMBER ''' 

def p_array_fill(p):
    ''' array_fill : VARIABLE COMMA array_fill 
                    | VARIABLE '''
def p_declaracion_struct_control(p):
    ''' declaracion_struct_control : while
                                    | if
                                    | loop'''
def p_while(p):
    ''' while : WHILE expresion_condicion bloque '''


        
#Donoso Bravo Luis Alejandro

def p_break(p):
    '''break : BREAK SEMICOLON'''
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
    '''if : IF condicion bloque
          | IF condicion bloque ELSE bloque'''

def p_condicion(p):
    '''condicion : expresion_condicion
                 | expresion_condicion logic_operator expresion_condicion'''

def p_logic_operator(p):
    '''logic_operator : AND
                      | OR'''

def p_comparacion(p):
    '''comparacion : EQUAL_EQUAL
                    | NOT_EQUAL
                    | GREATER
                    | GREATER_EQUAL
                    | LESS
                    | LESS_EQUAL'''


def p_expresion_condicion(p):
    '''expresion_condicion : boolean
                             | expresion_variable comparacion expresion_variable
                             | expresion_variable comparacion expresion_literal
                             | expresion_literal comparacion expresion_variable
                             | expresion_literal comparacion expresion_literal'''




def p_loop(p):
    '''loop : LOOP bloque'''


def p_declaracion_vector(p):
    '''declaracion_vector : LET VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND EQUAL expresion SEMICOLON
                          | LET VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND SEMICOLON
                          | LET  MUT VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND EQUAL expresion SEMICOLON
                          | LET MUT VARIABLE DOUBLE_POINT VEC LDIAMOND tipo RDIAMOND SEMICOLON'''

def p_funciones_vector(p):
    ''' funciones_vector : VARIABLE DOT PUSH LPAREN expresion RPAREN SEMICOLON
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

def p_funciones_hashmap(p):
    ''' funciones_hashmap : insert
                          | get
                          | contains_key'''

def p_insert(p):
    ''' insert : VARIABLE DOT INSERT LPAREN expresion COMMA expresion RPAREN SEMICOLON'''


def p_get(p):
    ''' get : VARIABLE DOT GET LPAREN expresion RPAREN SEMICOLON'''

def p_contains_key(p):
    ''' contains_key : VARIABLE DOT CONTAINS_KEY LPAREN expresion RPAREN SEMICOLON'''



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
