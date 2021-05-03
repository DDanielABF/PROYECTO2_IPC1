class factura:
    def __init__(self, fecha, paciente, doctor, consulta, operacion, internado, total):
        self.fecha = fecha
        self.paciente = paciente
        self.doctor = doctor
        self.consulta = consulta
        self.operacion = operacion
        self.internado = internado
        self.total = total

    def getFecha(self):
        return self.fecha

    def getPaciente(self):
        return self.paciente

    def getDoctor(self):
        return self.doctor


    def getConsulta(self):
        return self.consulta


    def getOperacion(self):
        return self.operacion

    def getInternado(self):
        return self.internado
    
    def getTotal(self):
        return self.total
 # metodos set----------------------------------------------


    def setFecha(self, fecha):
        self.fecha = fecha


    def setPaciente(self, paciente):
        self.paciente = paciente


    def setDoctor(self, doctor):
        self.doctor = doctor

    def setConsulta(self, consulta):
        self.consulta = consulta

    def setOperacion(self, operacion):
        self.operacion= operacion
    def setInternado(self,internado):
        self.internado= internado
    def setTotal(self, total):
        self.total = total