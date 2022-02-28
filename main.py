#Importamos la vista
from src.Cliente.Ventanas_ui import *
from src.Modelo.Archivo import FichaArchivo
import src.Utilidades.Filtrador as fl
import src.Utilidades.Nube as wd

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # Inicializamos el modelo para guardar el archivo que vayamos a usar.
    archivo = FichaArchivo()

    def __init__(self, *args, **kwargs):
        # Inicializamos las librerias de la interfaz grafica.
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # Llamamos al metodo de la clase padre para que se carguen los componentes.
        self.setupUi(self)

        #Evento de los botones (Ventana Filtrador).
        self.archivoBtn.clicked.connect(self.abrirFileChooserF)
        self.guardarBtn.clicked.connect(self.guardarArchivo)

        #Evento botones pestañas.
        self.tabWidget.tabBarClicked.connect(self.limpiarTodo)

        #Evento de los botones (Ventana Nube).
        self.archivo2Btn.clicked.connect(self.abrirFileChooserN)
        self.histogramaBtn.clicked.connect(self.crearHistograma)
    
    # Metodos Filtrar palabras
    def abrirFileChooserF(self):
        #Abrimos el file chooser que nos provee la libreria de PyQt y seleccionamos el archivo que querramos.
        file = QtWidgets.QFileDialog()
        file.setNameFilters(["CSV (*.csv)"])
        file.exec_()

        # Checamos si se selecciono algun archivo valido y asignamos el archivo en el modelo inicializado.
        if not file.selectedFiles():
            print('Vacio')
        else:
            # Asignamos el archivo seleccionado a la variable archivo de nuestro modelo.
            self.archivo.setArchivo(file.selectedFiles()[0])

            # Activamos el boton de guardar.
            self.guardarBtn.setEnabled(True)

    def guardarArchivo(self):
        #Abrimos un filechooser de tipo guardar.
        ruta = QtWidgets.QFileDialog().getSaveFileName(self, 'Guardar archivo')

        if ruta[0]:
            # Si se selecciono algo correr el metodo filtrar con el archivo, las palabras por filtrar y la ruta en donde se guardará.
            fl.C_Filtrador.filtrar(self.archivo.getArchivo(), self.textBrowser.toPlainText().split(), ruta[0])

            # Activamos la barra de progreso.
            self.progressBar.setVisible(True)

            # Llenamos la barra de progreso.
            for n in range(1, 101):
                self.progressBar.setProperty("value", n)
        else:
            # Si no se selecciono nada que imprima vacio.
            print('Vacio')

    def limpiarTodo(self):
        # Limpiamos todos los campos que se esten usando.
        self.textBrowser.clear()
        self.progressBar.setVisible(False)
        self.progressBar.setProperty("value", 0)
        self.guardarBtn.setEnabled(False)
    
    # Metodos nube de palabras
    def abrirFileChooserN(self):
        #Abrimos el file chooser que nos provee la libreria de PyQt y seleccionamos el archivo que querramos.
        file = QtWidgets.QFileDialog()
        file.setNameFilters(["CSV (*.csv)"])
        file.exec_()

        # Checamos si se selecciono algun archivo valido y asignamos el archivo en el modelo inicializado.
        if not file.selectedFiles():
            # Si no se seleccionó nada, que imprima vacio.
            print('Vacio')
        else:
            # Si se selecciono una archivo.
            # Asignamos el archivo seleccionado a la variable archivo de nuestro modelo.
            self.archivo.setArchivo(file.selectedFiles()[0])

            # Obtenemos la ruta del archivo seleccionado.
            archivo = self.archivo.getArchivo()

            # Corremos el metodo crearNube al que le pasaremos de parametros el archivo obtenido, la comlumna la cual se creara la nube 
            # ... y la cantidad de palabras.
            nube = wd.Nube.crearNube(archivo, 'Texto', 10000)

            # Guardamos la imagen generada en el directorio imagenes.
            nube.to_file('./Imagenes/wordcloud.png')

            # Imprimimos la imagen dentro de la interfaz.
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QtGui.QPixmap('./Imagenes/Wordcloud.png')
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)

            # Activamos el boton de histograma.
            self.histogramaBtn.setEnabled(True)
    
    def crearHistograma(self):
        # Obtenemos el archivo que se haya seleccionado.
        archivo = self.archivo.getArchivo()

        # Corremos el metodo crearHistograma el cual generará el histograma en base al archivo, la columna y el titulo que se quiera.
        wd.Nube.crearHistograma(archivo, 'Texto', 'Histograma')

        # Se imprime la imagen en la interfaz, que el metodo haya generado.
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QtGui.QPixmap('./Imagenes/grafica.png')
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()