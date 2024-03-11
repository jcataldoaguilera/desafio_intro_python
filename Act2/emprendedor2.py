# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-11
# RLAB-23-02-09-0044-2
#

# Advertencia
print("!!! Los valores ingresados deben ser enteros y sin separador de millares ¡¡¡")

# Definicion de variables
P = input("Ingrese precio de suscripción $: ")
Unorm = input("Ingrese número de usuarios normales: ")
Uprem = input("Ingrese número de usuarios premium: ")
GT = input("Ingrese el gasto total $: ")
# Definimos el data type
P = int(P)
Unorm = int(Unorm)
Uprem = int(Uprem)
GT = int(GT)
# Calculamos
UT = P*(Unorm+(Uprem*1.5))-GT

# Imprimir resultados
print(f"La rentabilidad es: ${UT}")