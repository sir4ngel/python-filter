class FichaArchivo:
    def __init__(self):
        self.archivo = None
    
    def setArchivo(self, archivo):
        self.archivo = archivo
    
    def getArchivo(self):
        return(self.archivo)