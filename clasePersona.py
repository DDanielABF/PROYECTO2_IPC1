class clasePersona:
    def __init__(self,nombre,apellido,nacimiento,sexo,usuario,contra,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo
        self.usuario = usuario
        self.contra = contra
        self.telefono = telefono

    def getnombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getNacimieto(self):
        return self.nacimiento

    def getSexo(self):
        return self.sexo
    def getUsuario(self):
        return self.usuario
    def getContra(self):
        return self.contra
    def getTelefono(self):
        return self.telefono
 #metodos set----------------------------------------------
    def setnombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento
    
    def setSexo(self, sexo):
        self.sexo = sexo
    def setUsuario(self, usuario):
        self.usuario = usuario
    def setContra(self, contra):
        self.contra = contra
    
    def setTelefono(self, telefono):
        self.telefono = telefono
