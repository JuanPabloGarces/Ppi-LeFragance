import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QPushButton, QApplication, QWidget
from PyQt5 import QtGui
from Selección import seleccion
from registrar import Ventana1
from recuperar import recuperar
class Login(QMainWindow):

    def __init__(self):
        super(Login, self).__init__()


        self.setWindowTitle("Fragance Storage")
        self.setStyleSheet("color: black")

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondo.01.png")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.setCentralWidget(self.fondo)

        self.letra1 = QFont()
        self.letra1.setFamily("Century")
        self.letra1.setPointSize(30)

        self.letra2 = QFont()
        self.letra2.setFamily("Andale Mono")
        self.letra2.setPointSize(14)

        self.letrero1 = QLabel(self)
        self.letrero1.setText("Login")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: #black	;")
        self.letrero1.move(620, 170)
        self.letrero1.setFixedWidth(400)
        self.letrero1.setFixedHeight(80)

        self.letrero2 = QLabel(self)
        self.letrero2.setText("Usuario")
        self.letrero2.setFont(self.letra2)
        self.letrero2.setStyleSheet("color: black	;")
        self.letrero2.move(500, 240)
        self.letrero2.setFixedWidth(80)
        self.letrero2.setFixedHeight(50)

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(350)
        self.editName.move(500, 280)
        self.editName.setStyleSheet("background-color:  #00FF0000 ")
        self.letrero3 = QLabel(self)

        self.letrero3.setText("Contraseña")
        self.letrero3.setFont(self.letra2)
        self.letrero3.setStyleSheet("color: black	;")
        self.letrero3.move(500, 340)
        self.letrero3.setFixedWidth(120)
        self.letrero3.setFixedHeight(50)

        self.editEmail = QLineEdit(self)
        self.editEmail.setFixedWidth(350)
        self.editEmail.move(500, 380)
        self.editEmail.setStyleSheet("background-color:  #00FF0000 ")

        self.boton1 = QPushButton(self)
        self.boton1.setText('Ingresar')
        self.boton1.setStyleSheet("background-color: #00FFFF; color: Black; border-radius: 12px;")
        self.boton1.setFont(self.letra2)
        self.boton1.move(500, 435)
        self.boton1.setFixedHeight(40)
        self.boton1.setFixedWidth(350)
        self.boton1.clicked.connect(self.metodo_ingresar)

        self.boton2 = QPushButton(self)
        self.boton2.setText('¿No tienes Cuenta? Registarte')
        self.boton2.setStyleSheet("background-color: #00FF0000; color: Black; border-radius: 20px;")
        self.boton2.setFont(self.letra2)
        self.boton2.move(500, 480)
        self.boton2.setFixedHeight(40)
        self.boton2.setFixedWidth(350)
        self.boton2.clicked.connect(self.metodo_Registrar)

        self.boton3 = QPushButton(self)
        self.boton3.setText('¿Olvidastes tu contraseña?')
        self.boton3.setStyleSheet("background-color: #00FF0000; color: Black;")
        self.boton3.setFont(self.letra2)
        self.boton3.move(500, 515)
        self.boton3.setFixedHeight(40)
        self.boton3.setFixedWidth(350)
        self.boton3.clicked.connect(self.metodo_Recuperar)

        self.setWindowIcon(QtGui.QIcon("imagenes/favicon.01.png"))

    def metodo_ingresar(self):
        self.hide()
        self.s1 = seleccion()
        self.s1.showMaximized()

    def metodo_Registrar(self):
        self.hide()
        self.r1 = Ventana1()
        self.r1.showMaximized()

    def metodo_Recuperar(self):
        self.hide()
        self.r2 = recuperar()
        self.r2.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    vlogin = Login()
    vlogin.showMaximized()
    sys.exit(app.exec_())







