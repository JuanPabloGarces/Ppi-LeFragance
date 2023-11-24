import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
from perfumeria1 import Perfumeria1
from perfumeria2 import Perfumeria2
from PyQt5 import QtGui
class seleccion(QMainWindow):

    def __init__(self):
        super(seleccion, self).__init__()

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/Fondo.Selección (2).png")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.setCentralWidget(self.fondo)



        self.letra1 = QFont()
        self.letra1.setFamily("pristina")
        self.letra1.setPointSize(20)

        self.boton1 = QPushButton(self)
        self.boton1.setFont(self.letra1)
        self.boton1.move(0, 0)
        self.boton1.setStyleSheet("background-color: #00FF0000;black: #00FF0000;")
        self.boton1.setFixedHeight(340)
        self.boton1.setFixedWidth(1500)
        self.boton1.clicked.connect(self.metodo_perfumeria1)

        self.boton2 = QPushButton(self)
        self.boton2.setText('Perfumeria 2')
        self.boton2.setFont(self.letra1)
        self.boton2.move(0, 345)
        self.boton2.setStyleSheet("background-color: #00FF0000;color: #00FF0000;")
        self.boton2.setFixedHeight(360)
        self.boton2.setFixedWidth(1500)
        self.boton2.clicked.connect(self.metodo_perfumeria2)

        self.setWindowIcon(QtGui.QIcon("imagenes/favicon.01.png"))

    def metodo_perfumeria1(self):
        self.hide()
        self.p1 = Perfumeria1()
        self.p1.showMaximized()

    def metodo_perfumeria2(self):
        self.hide()
        self.p2 = Perfumeria2()
        self.p2.showMaximized()








if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana2 = seleccion()
    ventana2.showMaximized()
    sys.exit(app.exec_())

