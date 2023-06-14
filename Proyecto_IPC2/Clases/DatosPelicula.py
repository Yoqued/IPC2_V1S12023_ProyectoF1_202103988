class peliculas:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora

    def getTitulo(self):
        return self.titulo
    def getDirector(self):
        return self.director
    def getAnio(self):
        return self.anio
    def getFecha(self):
        return self.fecha
    def getHora(self):
        return self.hora
    
    def setTitulo(self, titulo):
        self.titulo = titulo
    def setDirector(self, director):
        self.director = director
    def setAnio(self, anio):
        self.anio = anio
    def setFecha(self, fecha):
        self.fecha = fecha
    def setHora(self, hora):
        self.hora = hora

    def __repr__(self):
        return f"{self.titulo},{self.director},{self.anio},{self.fecha},{self.hora}"