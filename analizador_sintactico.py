import re
from colorama import Fore, init

init()


# Expresiones regulares
regex_llamado_libreria = re.compile(r'#include\s*<([a-zA-Z_]\w*\.\w+)>\s*')
regex_declaracion_variable = re.compile(r'\b(int|char|void|float)\s+((\w+\s*=\s*\d+(\.\d+)?|[a-zA-Z_]\w*\s*=\s*(\d+(\.\d+)?|[a-zA-Z_]\w*|"[^"]*"|\{[^}]*\}))(?:\s*,\s*(?=\w))?\s*)+;\s*$')
regex_declaracion_sin_asignacion = re.compile(r'\b(?:int|char|void|float)\s+([a-zA-Z_]\w*)\s*(?:,\s*[a-zA-Z_]\w*)*\s*;\s*$')
regex_do = re.compile(r'\bdo\s*{[^{}]*}?\s*$')
regex_while = re.compile(r'\bwhile\s*\(\s*(?!(\w+\s*=\s*[^=]))(?:[^=;{}()]*(?:==|!=|<=|>=|<|>|True|False)\s*[^=;{}()]*)\s*\)\s*{[^{}]*}?\s*$')
regex_for = re.compile(r'\bfor\s*\([^)]*\)\s*{[^{}]*}?\s*$')
regex_funcion = re.compile(r'\b(int|char|void|float)\s+([a-zA-Z_]\w*)\s*\([^)]*\)\s*{[^{}]*}?\s*$')
regex_llamada_funcion = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9]+,?(?:\s*[a-zA-Z_][a-zA-Z0-9]+,?)*)\s*\([^)]*\)\s*;$')
regex_switch =re.compile(r'\bswitch\s*\(\s*(?!(\w+\s*=\s*[^=]))(?:[^=;{}()]*(?:==|!=|<=|>=|<|>|True|False|\w*)\s*[^=;{}()]*)\s*\)\s*{[^{}]*}?\s*$')
regex_if =  re.compile(r'\bif\s*\(\s*(?!(\w+\s*=\s*[^=]))(?:[^=;{}()]*(?:==|!=|<=|>=|<|>|True|False)\s*[^=;{}()]*)\s*\)\s*{[^{}]*}?\s*$')
regex_else_if_optional_brace = re.compile(r'\belse\s+if\s*\(\s*(?!(\w+\s*=\s*[^=]))(?:[^=;{}()]*(?:==|!=|<=|>=|<|>|True|False)\s*[^=;{}()]*)\s*\)\s*{[^{}]*}?\s*$')
regex_asignacion_con_operadores = re.compile(r'\b([a-zA-Z_]\w*)\s*=\s*[^;]+\s*;\s*$')
regex_asignacion_operadores = re.compile(r'\b([a-zA-Z_]\w*)\s*([+\-*/%])?=\s*[^;]+\s*;\s*$')
regex_cierra_corchete = re.compile(r'^\s*}\s*$')
regex_incremento = re.compile(r'\b([a-zA-Z_]\w*\s*\+\+|--)\s*;$')
regex_return = re.compile(r'\breturn\s+([a-zA-Z_]\w*|\d+(\.\d+)?)?\s*;')
regex_else = re.compile(r'\belse\s*{\s*}?\s*$')

#Funciones de validación en las lineas
def validar_ops(linea):
    return regex_asignacion_operadores.search(linea) is not None
def validar_asignacion(linea):
    return regex_asignacion_con_operadores.search(linea) is not None
def validar_if(linea):
    return regex_if.search(linea) is not None
def validar_if_else(linea):
    return regex_else_if_optional_brace.search(linea) is not None
def validar_else(linea):
    return regex_else.search(linea) is not None
def validar_do(linea):
    return regex_do.search(linea) is not None
def validar_librerias_cabeceras(linea):
    return regex_llamado_libreria.search(linea) is not None
def validar_var_sin_asignacion(linea):
    return regex_declaracion_sin_asignacion.search(linea) is not None
def validar_while(linea): 
    return regex_while.search(linea) is not None
def validar_for(linea):
    return regex_for.search(linea) is not None
#def validar_abre_corchete(linea):
    #return regex_abre_corchete.search(linea) is not None
def validar_switch(linea):
    return regex_switch.search(linea) is not None
def validar_cierra_corchete(linea):
    return regex_cierra_corchete.search(linea) is not None

def validar_incremento(linea):
    return regex_incremento.search(linea) is not None

def validar_declaracion_variable(linea):
    return regex_declaracion_variable.search(linea) is not None


def validar_creacion_funcion(linea):
    return regex_funcion.search(linea) is not None

def validar_llamada_funcion(linea):
    return regex_llamada_funcion.search(linea) is not None



def es_salto_de_linea_o_espacio(linea):
    return not bool(linea.strip())

def validar_returns(linea):
    return regex_return.search(linea) is not None

def verificar_linea_codigo(linea):
    print(Fore.RESET+"===============================================")
    print(Fore.RESET + f"\n->Línea {i}:", linea.strip())

    #if validar_abre_corchete(linea):
        #print("Linea correcta.")
    if validar_cierra_corchete(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_if(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_if_else(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_asignacion(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_ops(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_var_sin_asignacion(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_do(linea):
       print(Fore.GREEN + "Linea correcta.")
    elif validar_else(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_declaracion_variable(linea):
       print(Fore.GREEN + "Linea correcta.")
   
    elif validar_creacion_funcion(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_llamada_funcion(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_switch(linea):
        print(Fore.GREEN + "Linea correcta")
    elif validar_while(linea):
        print(Fore.GREEN + "Linea correcta")
    elif validar_for(linea):
        print(Fore.GREEN + "Linea correcta")
  
    elif validar_incremento(linea):
        print(Fore.GREEN + "Linea correcta.")
    elif validar_librerias_cabeceras(linea):
        print(Fore.GREEN + "Linea correcta")
    elif validar_returns(linea):
        print(Fore.GREEN + "Linea correcta")
    elif es_salto_de_linea_o_espacio(linea):
        print("Espacio o salto de linea")
    else:
        print(Fore.RED + "Error en la línea.")

if __name__ == "__main__":
    archivo_codigo = "tokens.txt"  
    try:
        with open(archivo_codigo, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("El archivo no se encontró.")
    else:
        for i, linea in enumerate(lineas, 1):
            verificar_linea_codigo(linea)
