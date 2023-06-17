class peliculasFavorita:
    def __init__(self, correo, titulo):
        self.correo = correo
        self.titulo = titulo

    def getCorreo(self):
        return self.correo
    def getTitulo(self):
        return self.titulo
    
    def setCorreo(self, correo):
        self.correo = correo
    def setTitulo(self, titulo):
        self.titulo = titulo