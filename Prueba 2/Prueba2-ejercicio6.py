#Para un proyecto de iluminacio´n con celdas solares se dispone de una bater´ıa, la cual se carga de día y se descarga de noche. 
# La autonomía de una batería se define como el tiempo que demora en descargarse, el cual puede ser calculado mediante la ley de Peukert:
                    #    t= h / (ih/c)**k
'''
t   Autonomía de la batería en [Horas]
e   Capacidad de la batería en [Ampere-Hora]
H   Base de tiempo definida por el fabricante en [Horas]
I   Consumo en [Amperes]
k   Constante de Peukert

Se desea saber cuál es el número máximo de ampolletas que se puede conectar a esta batería de modo que puedan permanecer encendidas toda la noche, 
Es decir, que la autonomía sea mayor o igual a 8 horas. Se sabe que el consumo I, el cual es empleado en la ley de Peukert, viene dado por la suma de las
Potencias de cada ampolleta dividida por el voltaje  de la batería, es decir:

I = Potencia Ampolleta111 + Potencia Ampolleta112+.../ Voltaje Batería

Mientras que la constante de Peukert k tiene un valor de 1,15
Desarrolle un programa  Python que solicite los datos de la batería y luego solicite la potencia de cada ampolleta. 
El programa debe detenerse cuando no se puedan agregar más ampolletas debido a que la autonomía total sería menor que la autonomía requerida. 
Luego de solicitar la potencia  de cada ampolleta, el programa debe imprimir la autonomía, la cantidad de ampolletas y la potencia  total acumulada.

'''
c= int(input("Ingrese capacidad de la batería en Amperes: "))
h = int(input("Ingrese la base de tiempo definida por el fabricante en Horas: "))
voltaje = float(input("Ingrese el voltaje de la batería en Voltios: "))

consumo_total = 0
i_total = 0
ampolletas = 0

while True:
    try:
        potencia= float(input("Ingrese la potencia de la ampolleta en Watts: "))
    except ValueError:
        print("Ingrese un valor numérico válido")
        continue
    i = potencia / voltaje
    print(i)
    i_total += i
    print(i_total)
    t = h / (((i_total*h)/c)**1.15)
    print(t)
    ampolletas += 1
    i_total += i
    print(f"Autonomía total: {t} horas ")
    print(f"Cantidad de ampolletas: {ampolletas} ")
    print(f"potencia total acumulada: {i_total} Watts.")
    if t <= 8:
        break
