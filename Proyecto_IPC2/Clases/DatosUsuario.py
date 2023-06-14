class datos_usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contraseña):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contraseña = contraseña

    def getRol(self):
        return self.rol
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getTelefono(self):
        return self.telefono
    def getCorreo(self):
        return self.correo
    def getContraseña(self):
        return self.contraseña
    
    def setRol(self, rol):
        self.rol = rol
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setCorreo(self, correo):
        self.correo = correo
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    
    def __repr__(self):
        return f"{self.rol},{self.nombre},{self.apellido},{self.telefono},{self.correo},{self.contraseña}"