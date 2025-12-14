# ==========================================
# Programación Orientada a Objetos (POO)
# ==========================================

class ClimaDiario:
    """
    Clase que representa la información del clima de una semana.
    """
    
    def __init__(self):
        # Atributo privado (Encapsulamiento) para guardar los datos
        self.__temperaturas = []

    def ingresar_datos(self):
        """
        Método de la clase para pedir las temperaturas al usuario.
        """
        print("--- Ingreso de Temperaturas (POO) ---")
        for i in range(7):
            while True:
                try:
                    dato = input(f"Ingrese la temperatura del día {i + 1}: ")
                    temp = float(dato)
                    # Guardamos en la variable privada de la clase
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Error: Ingrese un valor numérico.")

    def calcular_promedio(self):
        """
        Método de la clase que calcula el promedio usando sus propios datos.
        """
        if not self.__temperaturas:
            return 0.0
        
        suma = sum(self.__temperaturas)
        promedio = suma / len(self.__temperaturas)
        return promedio

def main():
    # 1. Creamos el objeto (instancia de la clase)
    mi_clima = ClimaDiario()
    
    # 2. Usamos el método del objeto para pedir datos
    mi_clima.ingresar_datos()
    
    # 3. Usamos el método del objeto para calcular
    promedio = mi_clima.calcular_promedio()
    
    # 4. Mostramos resultados
    print(f"\nResultados Semanales (Objeto):")
    print(f"El promedio semanal es: {promedio:.2f} grados")

# Bloque para ejecutar el programa
if __name__ == "__main__":
    main()