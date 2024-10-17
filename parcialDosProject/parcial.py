def solicitar_datos_usuario():
    """Solicita al usuario los datos necesarios para el cálculo de la bonificación."""
    salario_base = float(input("Ingrese salario base mensual $: "))
    cargo = input("Ingrese el cargo del empleado: ").lower()
    desempeño = input("Ingrese el nivel de desempeño: ").lower()
    return salario_base, cargo, desempeño

def calcular_bonificacion(salario_base, cargo, desempeño):
    """Calcula la bonificación según el cargo y desempeño del empleado."""
    if cargo == 'directivo':
        if desempeño == 'alto':
            return salario_base * 0.20
        elif desempeño == 'medio':
            return salario_base * 0.10
        else:
            return 0
    elif cargo == 'operativo':
        if desempeño == 'alto':
            return salario_base * 0.15
        elif desempeño == 'medio':
            return salario_base * 0.05
        else:
            return 0
    else:
        return 0

def imprimir_resumen(salario_base, cargo, desempeño, bonificacion, total_a_recibir):

    print(f"----Resumen del Pago----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {desempeño.capitalize()}")
    print(f"Salario Base: ${salario_base:.0f}")
    print(f"Bonificación: ${bonificacion:.0f}")
    print(f"Total a Recibir: ${total_a_recibir:.0f}")
    print("------------------------------------")


salario_base, cargo, desempeño = solicitar_datos_usuario()


bonificacion = calcular_bonificacion(salario_base, cargo, desempeño)
total_a_recibir = salario_base + bonificacion

imprimir_resumen(salario_base, cargo, desempeño, bonificacion, total_a_recibir)