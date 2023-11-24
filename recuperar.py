import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from Cliente import Cliente


class recuperar(QMainWindow):

    def __init__(self, parent=None):
        super(recuperar, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

        self.setWindowIcon(QtGui.QIcon('imagenes/favicon.01.png'))

        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenfondo = QPixmap('imagenes/fondo.registro.svg')
        self.fondo.setPixmap(self.imagenfondo)
        self.fondo.setScaledContents(True)

        # hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenfondo.width(), self.imagenfondo.height())

        self.setCentralWidget(self.fondo)

        #distribucion layaout horizontal
        self.horizontal = QHBoxLayout()
        # margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)


        # --------LAYOUT IZQUIERDO-----------

        self.ladoIzquierdo = QFormLayout()

        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------LAYOUT DERECHO-------

        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText("Recuperar contraseña")
        self.letrero3.setFont(QFont("Century", 20))
        self.letrero3.setStyleSheet("color: black")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informarción para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        self.letrero4.setFont(QFont("Century", 10))

        self.letrero4.setStyleSheet("color: black; margin-bottom: 40px;"
                                    "margin top: 20px;"
                                    "border: 1px solid black;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        # ------1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        # ------2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        # ------3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)



        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(320)
        self.botonRecuperar.setStyleSheet("background-color: #00FFFF;"
                                            "color: black;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")

        self.ladoDerecho.addRow(self.botonRecuperar)

        self.horizontal.addLayout(self.ladoDerecho)

        self.horizontal.addLayout(self.ladoDerecho)

        # ---------- FINAL---------
        #el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de Registro")

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True






    def accion_botonRecuperar(self):


       self.datosCorrectos = True


       self.ventanaDialogo.setWindowTitle("Recuperar contraseña")


       if (
               self.pregunta1.text() == '' or
               self.pregunta2.text() == '' or
               self.pregunta3.text() == ''


       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe buscar las"
                                "\npreguntas de verificacion. Primero ingrese su"
                                "\ndocumento y luego presione el boton 'Buscar'")


           self.ventanaDialogo.exec_()


       if (
           self.pregunta1.text() != '' and
           self.respuesta1.text() == '' and
           self.pregunta2.text() != '' and
           self.respuesta2.text() == '' and
           self.pregunta3.text() != '' and
           self.respuesta3.text() == ''
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe ingresar"
                                "\nlas respuestas a cada pregunta.")


           self.ventanaDialogo.exec_()


       if (
           self.datosCorrectos
       ):
           self.file = open('datos/clientes.txt', 'rb')


           usuarios = []


           while self.file:
               linea = self.file.readline().decode('UTF-8')
               lista = linea.split(";")


               if linea == '':
                   break


               u = Cliente(
                   lista[0],
                   lista[1],
                   lista[2],
                   lista[3],
                   lista[4],
                   lista[5],
                   lista[6],
                   lista[7],
                   lista[8],
                   lista[9],
                   lista[10],
                )


               usuarios.append(u)


           self.file.close()


           existeDocumento = False


           resp1 = ''
           resp2 = ''
           resp3 = ''
           passw = ''


           for u in usuarios:


               if u.documento == self.documento.text():
                   existeDocumento = True


                   resp1 = u.respuesta1
                   resp2 = u.respuesta2
                   resp3 = u.respuesta3
                   passw = u.password


                   break


           if (
                   self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                   self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                   self.respuesta3.text().lower().strip() == resp3.lower().strip()
           ):


               self.accion_botonLimpiar()


               self.mensaje.setText("Contraseña: " + passw)


               self.ventanaDialogo.exec_()
           else:


               self.mensaje.setText("Las respuestas son incorrectas para estas"
                                    "\npreguntas de recuperacion de contraseña."
                                    "\nVuelva a intentarlo.")


               self.ventanaDialogo.exec_()



if __name__ == '__main__':
   app = QApplication(sys.argv)


   Recuperar = recuperar()


   Recuperar.show()


   sys.exit(app.exec_())
