import os
import PyQt5.QtGui
import pandas as pd
import  PyQt5
from matplotlib import pyplot as plt
import pathlib
from primeraG import *
from poblacion import *
from operadoresGeneticos import *

def evolucion_grafica(evol_fitness):
    df = pd.DataFrame(evol_fitness)
    # grafica de lineas
    plt.figure(figsize=[6, 6])
    plt.plot(df["generacion"], df["mejor"], color="green", label="Mejor Aptitud")
    plt.plot(df["generacion"], df["promedio"], color="orange", label="Promedio")
    plt.plot(df["generacion"], df["peor"], color="red", label="Peor Aptitud")
    plt.xlabel('Generaciones')  # override the xlabel
    plt.ylabel('Aptitud')  # override the ylabel
    plt.title('Evolucion de fitness')  # override the title
    plt.legend()
    rutaDestino = os.path.abspath(os.getcwd() + str('\imagenesEvolucion'))
    plt.savefig(rutaDestino + str('\Evolucion de fitness.jpg'))

def grafica_puntos(lista,limitesX,limitesY,i):
    data = []
    for j in lista:
        data.append([j['fenotipoX'], j['fenotipoY']])
    x, y = zip(*data)
    fig, ax = plt.subplots()
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.title("Generacion: " + str(i + 1) + " -- Individuos: " + str(len(lista)))
    plt.xlim(limitesX[0], limitesX[1])
    plt.ylim(limitesY[0], limitesY[1])
    plt.xlabel("X")
    plt.ylabel("Y")
    ax.scatter(x, y)
    rutaDestino = os.path.abspath(os.getcwd()+str('\imagenesSolucion'))
    plt.savefig(rutaDestino+str('\{0}.jpg'.format(str(i+1))))
    print("termino")


def crear_exel(mejores_individuos):
    try:
        df = pd.DataFrame(mejores_individuos)
        print(df)
        name = PyQt5.QtWidgets.QFileDialog.getSaveFileName(None, "save csv file", "","CSV files(*.csv)")  # obtener ruta de guardado
        df.to_csv(name[0], index=False)  # guardar el archivo
    except:
        print("no selecciono archivo a guardar")


def inicializarAlgoritmo(limitesX,limitesY,resolucion,poblacionInicial,generaciones,poblacion_max,pro_individuo,pro_genotipo):
    lista = primeraGen(resolucion, poblacionInicial, limitesX, limitesY)
    tamañoX = tamañoIntervalo(limitesX)
    tamañoY = tamañoIntervalo(limitesY)
    cantidadX = cantidadValores(resolucion, tamañoX)
    cantidadY = cantidadValores(resolucion, tamañoY)
    bitsX = cantidadBits(cantidadX)
    bitsY = cantidadBits(cantidadY)
    deltaX = valorDelta(tamañoX, bitsX)
    deltaY = valorDelta(tamañoY, bitsY)
    evol_fitness = []
    mejores_individuos = []
    for i in range(generaciones):
        evol_fitness.append(evolucion_fitness(lista, i))
        mejores_individuos.append(mejor_individuo(lista))
        grafica_puntos(lista,limitesX,limitesY,i)
        lis = prox_generacion(lista, pro_individuo, pro_genotipo, limitesX, limitesY, resolucion, bitsX, bitsY, cantidadX,cantidadY, deltaX, deltaY)
        if len(lis) > poblacion_max:
            lista = poda(lis, poblacion_max)
        else:
            lista = lis

    crear_exel(mejores_individuos)
    evolucion_grafica(evol_fitness)
