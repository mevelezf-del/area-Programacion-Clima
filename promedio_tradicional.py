# ==========================================
# Programación Tradicional: Promedio de Clima
# ==========================================

def ingresar_temperaturas_diarias():
    """
    Función para solicitar al usuario las temperaturas de los 7 días.
    Retorna una lista de números.
    """
    temperaturas = []
    print("--- Ingreso de Temperaturas (Tradicional) ---")
    
    # Ciclo para pedir los 7 días
    for i in range(7):
        while True:
            try:
                # Pedimos el dato y lo convertimos a decimal (float)
                dato = input(f"Ingrese la temperatura del día {i + 1}: ")
                temp = float(dato)
                temperaturas.append(temp)
                break 
            except ValueError:
                print("Error: Debes escribir un número.")
    
    return temperaturas

def calcular_promedio_semanal(lista):
    """
    Función que recibe la lista y calcula el promedio.
    """
    cantidad = len(lista)
    if cantidad == 0:
        return 0.0
    
    suma = sum(lista)
    promedio = suma / cantidad
    return promedio

def main():
    """
    Función principal que organiza el programa.
    """
    # 1. Llamamos a la función para pedir datos
    datos = ingresar_temperaturas_diarias()
    
    # 2. Llamamos a la función para calcular
    promedio = calcular_promedio_semanal(datos)
    
    # 3. Mostramos el resultado
    print(f"\nResultados Semanales:")
    print(f"Temperaturas: {datos}")
    print(f"El promedio es: {promedio:.2f} grados")

# Bloque para ejecutar el programa
if __name__ == "__main__":
    main()