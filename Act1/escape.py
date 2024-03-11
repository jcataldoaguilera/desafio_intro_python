# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-11
# RLAB-23-02-09-0044-2
#

# Librerias
from math import sqrt

# Definicion y reciclaje de Variables
radio = input("Ingrese el radio en Kilometros: ")
cons_g = input("Ingrese la constante g: ")
# Definimos data type de las variables
radio = int(radio)
cons_g = float(cons_g)
# A nivel de formula, el radio se expresa en metros, pero en el input se nos solicita ingresar el radio en Kilometros,
# por lo que multiplicamos el input por 1000 para transformar la unidad.
escape = sqrt(2*cons_g*(1000*radio))
# Redondeamos decimales
escape = round(escape,2)

# Imprimir resultados
print(f"La velocidad de Escape es {escape} [m/s]")
