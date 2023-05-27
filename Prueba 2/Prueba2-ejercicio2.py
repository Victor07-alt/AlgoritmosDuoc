n = int(input("Ingrese el valor de 'n': "))
cantidad_productos = int(input("Ingrese la cantidad de productos: "))

precios = []
for i in range(cantidad_productos):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    precios.append(precio)

descuento = 0.2  # Descuento inicial
precio_total = sum(precios)
descuento_total = 0
grupos = (len(precios) + n - 1) // n #determinar la cantidad de grupos necesarios y la cantidad de grupos en los cuales se aplicará un descuento.
grupos_descuento = grupos - 1

for i in range(grupos):
    grupo = precios[i * n:(i + 1) * n]

    if len(grupo) == n:
        descuento_aplicado = descuento * sum(grupo)
        descuento_total += descuento_aplicado
        precio_total -= descuento_aplicado

    if i < grupos_descuento:
        descuento /= 2

precio_final = int(precio_total)

if len(precios) < n:
    print("La cantidad de productos es menor que n. No se aplica descuento.")
else:
    print(f"Precio total sin descuento: {precio_total + descuento_total}")
    print(f"Descuento total: {descuento_total}")
    print(f"Precio final después del descuento: {precio_final}")
