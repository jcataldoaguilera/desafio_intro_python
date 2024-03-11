# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-11
# RLAB-23-02-09-0044-2
#

# Librerias
from math import sqrt

# Definicion de Variables
radio = int(input("Ingrese el radio en Kilometros: "))
cons_g = float(input("Ingrese la constante g: "))

# A nivel de formula, el radio se expresa en metros, pero en el input se nos solicita ingresar el radio en Kilometros,
# por lo que multiplicamos el input por 1000 para transformar la unidad.
escape = sqrt(2*cons_g*(1000*radio))
# Redondeamos decimales
escape = round(escape,2)

# Imprimir resultados
print(f"La velocidad de Escape es {escape} [m/s]")
