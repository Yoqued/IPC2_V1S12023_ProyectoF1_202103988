class categorias:
    def __init__(self, categoria, nombrepeli):
        self.nombrepeli = nombrepeli
        self.categoria = categoria
    
    def getNombre(self):
        return self.nombrepeli
    def getCate(self):
        return self.categoria
    
    def setNombre(self, nombrepeli):
        self.nombrepeli = nombrepeli
    def setCate(self, categoria):
        self.categoria = categoria
