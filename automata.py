import re

class Token:
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna
    
    def __str__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}', linea={self.linea}, columna={self.columna})"

class Lexer:
    def __init__(self):
        self.palabras_reservadas = {
            "si", "sino", "mientras", "para", 
            "leer", "escribir",  
            "entero", "decimal", "cadena", "booleano", 
            "verdadero", "falso", 
            "inicio" 
        }
        self.operadores_logicos = {"&&", "||", "!", "==", ">=", "<=", ">", "<", "!="}
        self.operadores_asignacion = {"=", "+=", "-=", "*=", "/="}
        self.operadores_matematicos = {"+", "-", "*", "/"}
        self.separadores = {"(", ")", "{", "}", ";", ","}
        
        # Construir expresión regular para tokens
        # IMPORTANTE: El orden importa - los operadores más largos deben ir primero
        self.token_specs = [
            ('NUMERO', r'\d+(\.\d+)?'),  # Números enteros o decimales
            ('LOGICO', r'(&&|\|\||==|!=|>=|<=|>|<|!)'),  # Operadores lógicos (PRIMERO)
            ('ASIGNACION', r'(\+=|-=|\*=|/=|=)'),  # Operadores de asignación (DESPUÉS)
            ('MATEMATICO', r'[\+\-\*/]'),  # Operadores matemáticos
            ('SEPARADOR', r'[\(\)\{\};,]'),  # Separadores
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores
            ('STRING', r'\"([^\\\"]|\\.)*\"'),  # Cadenas entre comillas
            ('ESPACIO', r'[ \t\r\n]+'),  # Espacios en blanco
            ('ERROR', r'.'),  # Cualquier otro carácter es error
        ]
        
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specs)
        self.re_token = re.compile(self.token_regex)
    
    def tokenize(self, codigo):
        linea = 1
        columna = 1
        tokens = []
        for match in self.re_token.finditer(codigo):
            tipo = match.lastgroup
            valor = match.group(tipo)
            
            # Actualizar posición
            inicio_columna = columna
            lineas = valor.split('\n')
            if len(lineas) > 1:
                linea += len(lineas) - 1
                columna = len(lineas[-1]) + 1
            else:
                columna += len(valor)
            
            # Ignorar espacios
            if tipo == 'ESPACIO':
                continue
            
            # Determinar el tipo exacto del token
            tipo_final = tipo
            if tipo == 'ID' and valor in self.palabras_reservadas:
                tipo_final = 'PALABRA_RESERVADA'
            elif tipo == 'ASIGNACION':
                tipo_final = 'OPERADOR_ASIGNACION'
            elif tipo == 'LOGICO':
                tipo_final = 'OPERADOR_LOGICO'
            elif tipo == 'MATEMATICO':
                tipo_final = 'OPERADOR_MATEMATICO'
            elif tipo == 'SEPARADOR':
                tipo_final = 'SEPARADOR'
            elif tipo == 'NUMERO':
                tipo_final = 'NUMERO'
            elif tipo == 'STRING':
                tipo_final = 'STRING'
            elif tipo == 'ERROR':
                raise ValueError(f"Carácter inesperado '{valor}' en línea {linea}, columna {inicio_columna}")
            
            tokens.append(Token(tipo_final, valor, linea, inicio_columna))
        
        return tokens

def analizar_archivo(nombre_archivo):
    lexer = Lexer()
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
        
        tokens = lexer.tokenize(codigo)
        
        print("\nResultado del análisis léxico:\n")
        print("{:<20} {:<15} {:<10} {:<10}".format('Tipo', 'Valor', 'Línea', 'Columna'))
        print("-" * 55)
        for token in tokens:
            print("{:<20} {:<15} {:<10} {:<10}".format(
                token.tipo, token.valor, token.linea, token.columna))
        
        return tokens
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
        return []
    except ValueError as e:
        print(f"Error: {str(e)}")
        return []

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo a analizar: ")
    analizar_archivo(nombre_archivo)