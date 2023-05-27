# Datos de la batería
capacidad_bateria = float(input("Capacidad de la batería (AH): "))
voltaje_bateria = float(input("Voltaje de la batería (volt): "))
base_tiempo = float(input("Base de tiempo (Horas): "))

# Variables iniciales
autonomia_requerida = 8  # Autonomía requerida en horas
potencia_total = 0
cantidad_ampolletas = 0

while True:
    potencia_ampolleta = float(input(f"Potencia ampolleta {cantidad_ampolletas + 1} (Watt): "))

    # Calcular el consumo según la ley de Peukert
    consumo = (potencia_total + potencia_ampolleta) / voltaje_bateria

    # Calcular la autonomía
    autonomia = capacidad_bateria / (consumo ** 1.15)

    if autonomia < autonomia_requerida:
        break

    potencia_total += potencia_ampolleta
    cantidad_ampolletas += 1

    print(f"Autonomía: {autonomia:.3f} [Horas]. Ampolletas: {cantidad_ampolletas}. Potencia Total: {potencia_total:.3f} [Watt]")

print(f"Total de Ampolletas soportadas: {cantidad_ampolletas}")
