import ply.lex as lex

# Analizador léxico para Rust

# Diccionario de palabras reservadas
reserved = {
    # Xavier Magallanes
    'println': 'PRINT',
    'let': 'LET',
    'mut': 'MUT',
    'fn': 'FN',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'loop': 'LOOP',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'true': 'TRUE',
    'false': 'FALSE',
    'struct': 'STRUCT',
    'enum': 'ENUM',
    'impl': 'IMPL',
    'use': 'USE',
    'vec': 'VEC',
    'static': 'STATIC',
    'type': 'TYPE',
    'ref': 'REF',
    'match': 'MATCH',
    'as': 'AS',
    'mod': 'MOD',
    'trait': 'TRAIT',
    'pub': 'PUB',
    'i8' : 'INT8',
    'i16' : 'INT16',
    'i32' : 'INT32',
    'i64' : 'INT64',
    'u8' : 'UINT8',
    'u16' : 'UINT16',
    'u32' : 'UINT32',
    'u64' : 'UINT64',
    'f32' : 'FLOAT32',
    'f64' : 'FLOAT64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'str' : 'STR',
    'const' : 'CONST',
    'push' : 'PUSH',
    'pop' : 'POP',
    'len' : 'LEN',
    'clear' : 'CLEAR',
    'is_empty' : 'IS_EMPTY',
    'get' : 'GET',
    'set' : 'SET',
    'remove' : 'REMOVE',
    'swap' : 'SWAP',
    'reverse' : 'REVERSE',
    'iter' : 'ITER',
    'array' : 'ARRAY',
}

# Sequencia de tokens, puede ser lista o tupla
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
          'LBRACKET', 'RBRACKET', 'VARIABLE', 'STRING', 'SEMICOLON',
          'EXCLAMATION', 'EQUAL', 'COMMA', 'L_BRACKET', 'R_BRACKET', 'DOUBLE_POINT', 'POINT', 'PERCENTAGE', 'AND', 'OR', 'BITAND' , 'BITOR', 'BITXOR',
          'LDIAMOND', 'RDIAMOND', 'GREATER', 'LESS', 'EQUAL_EQUAL', 'NOT_EQUAL', 'LESS_EQUAL', 'GREATER_EQUAL', 'ARROW', 'DOT') + tuple(reserved.values())

# Exp Regulares para tokens de símbolos
# Xavier Magallanes
t_PLUS = r'\+'
t_MINUS = r'\-'
t_COMMA = r'\,'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_NUMBER = r'\d+'
t_SEMICOLON = r'\;'
t_EXCLAMATION = r'\!'
t_EQUAL = r'\='
# Fausto Jacome
t_L_BRACKET = r'\['
t_R_BRACKET = r'\]'
t_DOUBLE_POINT = r'\:'
t_POINT = r'\.'
t_PERCENTAGE = r'\%'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_BITAND = r'\&'
t_BITOR = r'\|'
t_BITXOR = r'\^'
# Donoso Bravo Luis Alejandro
t_LDIAMOND = r'\<'
t_RDIAMOND = r'\>'
t_GREATER = r'\>'
t_LESS = r'\<'
t_EQUAL_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='
t_LESS_EQUAL = r'\<\='
t_GREATER_EQUAL = r'\>\='
t_ARROW = r'\->'
t_DOT = r'\.'



# Para contabilizar nro de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_VARIABLE(t):
    r'(_{1}|[a-zA-Z]{1})[a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_STRING(t):
    r'\"{1}.*"{1}'
    t.type = reserved.get(t.value, 'STRING')
    return t


def t_COMMENT(t):
    r'\/{2}.*'
    pass
    # No return value. Token discarded

#Donoso Bravo Luis Alejandro
def t_Option(t):
    r'Option'
    t.type = reserved.get(t.value, 'OPTION')
    return t

def t_Some(t):
    r'Some'
    t.type = reserved.get(t.value, 'SOME')
    return t

def t_None(t):
    r'None'
    t.type = reserved.get(t.value, 'NONE')
    return t




# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


# Presentación de errores léxicos
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Contruir analizador
lexer = lex.lex()

data = '''
    let mut x = 5;
    let y = 10;
    let z = x + y;
    println!("El valor de z es: {}", z);
    let mut contador = 0;
    let resultado = loop {
        contador += 1;
        if contador == 10 {
            break contador * 2;
}
};
    println!("El resultado es {}", resultado);
    let a = [10, 20, 30, 40, 50];
    for elemento in a.iter() {
        println!("El valor es: {}", elemento);
}
    for numero in (1..4).rev() {
        println!("{}!", numero);
}

use rand::Rng;

fn main() {

let mut range = rand::thread_rng();

let num: i32 = range.gen();

println!("Random: {}", n1);
}

// Donoso Bravo Luis Alejandro
fn binary_search<T>: Ord>(array: &[T], target: &T) -> Option<usize> {
    let mut left = 0;
    let mut right = array.len() - 1;

    while left <= right {
        let mid = left + (right - left) / 2;
        
        if array[mid] == *target {
            return Some(mid);
        } else if array[mid] < *target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    None
}

fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let target = 6;
    
    if let Some(index) = binary_search(&numbers, &target) {
        println!("Target {} found at index {}", target, index);
    } else {
        println!("Target {} not found", target);
    }
}

    '''

# Datos de entrada
lexer.input(data)

# Tokenizador
while True:
    tok = lexer.token()
    if not tok:
        break  # Rompe
    print(tok)
