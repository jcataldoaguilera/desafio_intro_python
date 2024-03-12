# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-11
# RLAB-23-02-09-0044-2
#

# Advertencia
print("!!! Los valores ingresados deben ser enteros y sin separador de millares ¡¡¡")

# Definicion de variables
P = int(input("Ingrese precio de suscripción $: "))
U = int(input("Ingrese número de usuarios: "))
GT = int(input("Ingrese el gasto total $: "))
Upas = int(input("Ingrese las utilidades del año anterior $: "))

# Validación de variable
if Upas > 0 :
    UT = P*U-GT
    Ur = UT/Upas
    # Imprimir resultados
    print(f"La rentabilidad es: ${UT}")
    print(f"La razón entre las utilidades actuales y las del año anterior es {round(Ur,2)}")
else:
    print("Las utilidades del año anterior no pueden ser iguales a 0")
    