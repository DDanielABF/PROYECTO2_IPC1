class Citas:
      def __init__(self,id,paciente,fecha,doctor,estado,motivo,hora):
        self.id = id
        self.paciente = paciente
        self.fecha = fecha
        self.doctor = doctor
        self.estado = estado
        self.motivo = motivo
        self.hora = hora
      def getId(self):
        return self.id

      def getPaciente(self):
        return self.paciente
     
      def getFecha(self):
        return self.fecha


      def getDoctor(self):
        return self.doctor

      def getEstado(self):
        return self.estado


      def getMotivo(self):
        return self.motivo
      def getHora(self):
        return self.hora

 # metodos set----------------------------------------------


      def setId(self, id):
        self.id = id


      def setPaciente(self, paciente):
        self.paciente = paciente

      def setFecha(self, fecha):
        self.fecha = fecha
      
      def setDoctor(self, doctor):
        self.doctor = doctor



      
      def setEstado(self, estado):
        self.estado = estado

       

      def setMotivo(self, motivo):
        self.motivo= motivo    

      def setHora(self,hora):
        self.hora = hora