# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventanas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.archivoBtn = QtWidgets.QPushButton(self.tab_5)
        self.archivoBtn.setObjectName("archivoBtn")
        self.gridLayout_2.addWidget(self.archivoBtn, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 7, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 10, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_5)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.gridLayout_2.addWidget(self.progressBar, 11, 0, 1, 1)
        self.guardarBtn = QtWidgets.QPushButton(self.tab_5)
        self.guardarBtn.setEnabled(False)
        self.guardarBtn.setObjectName("guardarBtn")
        self.gridLayout_2.addWidget(self.guardarBtn, 12, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.line_3 = QtWidgets.QFrame(self.tab_6)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tab_6)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.archivo2Btn = QtWidgets.QPushButton(self.tab_6)
        self.archivo2Btn.setObjectName("archivo2Btn")
        self.verticalLayout_2.addWidget(self.archivo2Btn)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.histogramaBtn = QtWidgets.QPushButton(self.tab_6)
        self.histogramaBtn.setEnabled(False)
        self.histogramaBtn.setObjectName("histogramaBtn")
        self.gridLayout_4.addWidget(self.histogramaBtn, 2, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_6)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 2, 0, 1, 5)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 3)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 4, 0, 1, 2)
        self.archivo3Btn = QtWidgets.QPushButton(self.tab)
        self.archivo3Btn.setObjectName("archivo3Btn")
        self.gridLayout_5.addWidget(self.archivo3Btn, 5, 0, 1, 5)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setVisible(False)
        self.gridLayout_5.addWidget(self.progressBar_2, 6, 0, 1, 5)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 7, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_5.addWidget(self.line_5, 8, 0, 1, 5)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 9, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 9, 3, 1, 1)
        self.txIniciales = QtWidgets.QTextEdit(self.tab)
        self.txIniciales.setObjectName("txIniciales")
        self.gridLayout_5.addWidget(self.txIniciales, 10, 0, 1, 3)
        self.txEntrenamiento = QtWidgets.QTextEdit(self.tab)
        self.txEntrenamiento.setObjectName("txEntrenamiento")
        self.gridLayout_5.addWidget(self.txEntrenamiento, 10, 3, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 11, 0, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 12, 0, 1, 5)
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 13, 0, 1, 2)
        self.txPalabrasClave = QtWidgets.QLineEdit(self.tab)
        self.txPalabrasClave.setObjectName("txPalabrasClave")
        self.gridLayout_5.addWidget(self.txPalabrasClave, 13, 2, 1, 3)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 14, 0, 1, 1)
        self.txRes = QtWidgets.QLineEdit(self.tab)
        self.txRes.setObjectName("txRes")
        self.gridLayout_5.addWidget(self.txRes, 14, 1, 1, 3)
        self.enviarRedBtn = QtWidgets.QPushButton(self.tab)
        self.enviarRedBtn.setObjectName("enviarRedBtn")
        self.enviarRedBtn.setEnabled(False)
        self.gridLayout_5.addWidget(self.enviarRedBtn, 14, 4, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionFiltrar = QtWidgets.QAction(MainWindow)
        self.actionFiltrar.setObjectName("actionFiltrar")
        self.actionNube_de_palabras = QtWidgets.QAction(MainWindow)
        self.actionNube_de_palabras.setObjectName("actionNube_de_palabras")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#777777;\">Filtrar palabras clave</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Archivo a importar</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Seleccione el archivo (CSV) a importar.</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Buscar en su computadora:</span></p></body></html>"))
        self.archivoBtn.setText(_translate("MainWindow", "Elegir archivo"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Palabras clave</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Escriba las palabras clave que desea filtrar de su archivo.</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Para filtrar las palabras, por favor separelas con espacios. Por ejemplo: <span style=\" font-weight:600;\">quiero estas palabras</span></p></body></html>"))
        self.guardarBtn.setText(_translate("MainWindow", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Filtrar palabras"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#777777;\">Nube de palabras</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Archivo a importar</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Seleccione el archivo (CSV) a importar.</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Buscar en su computadora:</span></p></body></html>"))
        self.archivo2Btn.setText(_translate("MainWindow", "Elegir archivo"))
        self.histogramaBtn.setText(_translate("MainWindow", "Ver histograma"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Nube de palabras"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#777777;\">Red neuronal</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Archivo a importar</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Seleccione el archivo (CSV) a importar.</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Buscar en su computadora:</span></p></body></html>"))
        self.archivo3Btn.setText(_translate("MainWindow", "Elegir archivo"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Pesos sinapticos</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Iniciales</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Con entrenamiento</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Palabras clave</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Escribe alguna de estas palabras clave y escribelas separadas con un espacio: </span><span style=\" font-size:9pt; font-weight:600;\">cocina chef platillo</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">restaurante mesero comida favorita</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Respuesta:</span></p></body></html>"))
        self.enviarRedBtn.setText(_translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Red neuronal"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionFiltrar.setText(_translate("MainWindow", "Filtrar"))
        self.actionNube_de_palabras.setText(_translate("MainWindow", "Nube de palabras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

