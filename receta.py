class receta:
    def __init__(self, fecha, paciente, padecimiento, descripcion):
        self.fecha = fecha
        self.paciente = paciente
        self.padecimiento = padecimiento
        self.descripcion = descripcion
        
    def getFecha(self):
        return self.fecha

    def getPaciente(self):
        return self.paciente

    def getPadecimiento(self):
        return self.padecimiento


    def getDescripcion(self):
        return self.descripcion


 # metodos set----------------------------------------------


    def setFecha(self, fecha):
        self.fecha = fecha


    def setPaciente(self, paciente):
        self.paciente = paciente


    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    