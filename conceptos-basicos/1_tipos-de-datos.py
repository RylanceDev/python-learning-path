#Exploración de tipos de datos
#Dev: Rylance

# 1. Strings simples y dobles (Línea única)
"Hola mundo"
'Bienvenidos'

# 1.1 Docstrings (Strings de múltiples líneas para datos estructurados)
"""Tus datos son:
        nombre : Daniel
        apellido : Llanos"""

# 1.2 Alternativa para bloques de texto
'''
ESTADO DEL JUGADOR:
    ID      : #001
    Alias   : Vantix
    Nivel   : 1 (Básico)
    Estatus  : Online
'''

# 2. int (entero)
edad = 25               # int (positivo)
temperatura = -10       # int (negativo)
cantidad_clases = 0     # int (cero)

# 3. float (decimal)
precio = 19.99              # float (con decimales)
gravedad = 9.8              # float (constante física)
saldo = -150.50             # float (saldo negativo)
entero_como_float = 40.0    # float (aunque el valor sea entero, el .0 lo cambia)

# 4. bool (booleano)
es_estudiante = True    # bool (Verdadero)
tiene_deuda = False     # bool (Falso)

# Nota: Estos bloques no se mostrarán en consola a menos que uses print()
print(saldo)        # Muestra el valor de la variable 'saldo' en la terminal (-150.5)
