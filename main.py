import sys
import PyQt5
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator
from view.main import Ui_AlgoritmoGenetico as ventanaPrincipal
from inicio import inicializarAlgoritmo

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    validarEntradas(ventana)
    pixmap = QPixmap('resources/mifuncion.png') # cargamos la imagen
    ventana.funcionMostrar.setPixmap(pixmap) # lo cargamos al label
    ventana.funcionMostrar.setScaledContents(True) # lo adaptamos
    ventana.resultado.clicked.connect(lambda: AG(ventana))

def validarEntradas(ventana):
    ventana.a1.setValidator(QDoubleValidator())
    ventana.a2.setValidator(QDoubleValidator())
    ventana.b1.setValidator(QDoubleValidator())
    ventana.b2.setValidator(QDoubleValidator())
    ventana.resolucion.setValidator(QDoubleValidator())
    ventana.pobin.setValidator(QIntValidator())
    ventana.pobmax.setValidator(QIntValidator())
    ventana.numGeneraciones.setValidator(QIntValidator())
    ventana.prob_sel_ind.setValidator(QDoubleValidator())
    ventana.prob_mut_ind.setValidator(QDoubleValidator())

def cargarAjuste(ventana):
    try:
        datos = {
            "limitesX": (float(ventana.a1.text()), float(ventana.a2.text())),
            "limitesY": (float(ventana.b1.text()), float(ventana.b2.text())),
            "resolucion": float(ventana.resolucion.text()),
            "poblacionInicial": float(ventana.pobin.text()),
            "poblacionMaxima": float(ventana.pobmax.text()),
            "numeroGeneraciones": int(ventana.numGeneraciones.text()),
            "prob_sel_ind": float(ventana.prob_sel_ind.text()),
            "prob_mut_ind": float(ventana.prob_mut_ind.text())
        }
    except:
        print("falta algun dato")
    '''datos = {
            "limitesX": ((-10,10)),
            "limitesY": ((-10,10)),
            "resolucion": 0.001,
            "poblacionInicial":3,
            "numeroGeneraciones": 3,
            "poblacionMaxima": 7,
            "prob_sel_ind": 0.5,
            "prob_mut_ind": 0.5
    }'''
    return datos

def AG(ventana):
    datos = cargarAjuste(ventana)
    inicializarAlgoritmo(datos["limitesX"],datos["limitesY"],datos["resolucion"],datos["poblacionInicial"],datos["numeroGeneraciones"],datos["poblacionMaxima"],datos["prob_sel_ind"],datos["prob_mut_ind"])

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()
