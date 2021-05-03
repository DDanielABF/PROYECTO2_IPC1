from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS

from flask.globals import request
from clasePersona import clasePersona
from doctores import doctores
from enfermeras import enfermeras
from medicamentos import medicamentos
from Citas import Citas
from factura import factura
from receta import receta

import json
import csv
cont =0
RECETAS = []
FACTURAS = []
CITAS = []
personas = []
Doctores = []
ENFERMERAS = []
MEDICAMENTOS = []
app = Flask(__name__)
CORS(app)
# datos de prueba
personas.append(clasePersona('Daniel', 'Alexander', '15/11/2000',
                'Masculino', 'Daniel', 'siuu2020', '57183673'))
personas.append(clasePersona('Gary', 'Alejandro', '15/11/2003',
                'Masculino', 'umpa', 'siuu2010', '57183543'))
personas.append(clasePersona('Mark', 'Alero', '15/11/2010',
                'Masculino', 'lumpa', 'siuu2030', '57183642'))
personas.append(clasePersona('El ', 'Bicho', '15/11/2001',
                'Masculino', 'johncena', 'siuu2420', '57183213'))
Doctores.append(doctores('Jonatan', 'Arturo', '29/09/1992',
                'masculino', 'jonz', 'joymar', 'corazon', '45679697'))
Doctores.append(doctores('Mauricio', 'Icardi', '12/07/1995',
                'masculino', 'mau', 'icardi', 'pulmones', '4123697'))
ENFERMERAS.append(enfermeras('Daniela', 'Alexandra', '15/10/1999',
                             'Femenino', 'Daniela', 'gg2020', '57182803'))
ENFERMERAS.append(enfermeras('Maria', 'de los Angeles', '04/07/2000',
                             'Femenino', 'red', 'f2019', '40245048'))
MEDICAMENTOS.append(medicamentos('0', 'paracetamol', 'Q.24', 'drogas', '3'))

# datos totales


@app.route('/', methods=['GET'])
def rutainicialpg():
    print("hola mundo")
    objeto = {

        "Nombre": "Daniel   ",
        "Edad": 22,
        "vivo": True

    }
    return(jsonify(objeto))


# metodopost


@app.route('/', methods=['POST'])
def rutainicialp():
    print("hola mundo")
    objeto = {

        "Nombre": "carlos",
        "Edad": 20,
        "vivo": False

    }
    return(jsonify(objeto))

 # Iniciar Sesion


@app.route('/login/<user>/<password>')
def iniciar_sesion(user, password):
    print(user)
    print(password)
    global personas
    for x in personas:
        if x.getContra() == password and x.getUsuario() == user:
            return json.dumps(x.__dict__)
    return '{"nombre":"false"}'


@app.route('/loginDoctores/<user>/<password>')
def iniciar_sesionDoc(user, password):
    print(user)
    print(password)
    global Doctores
    for x in Doctores:
        if x.getContra() == password and x.getUsuario() == user:
            return json.dumps(x.__dict__)
    return '{"nombre":"false"}'


@app.route('/loginEnfermeras/<user>/<password>')
def iniciar_sesionEnf(user, password):
    print(user)
    print(password)
    global ENFERMERAS
    for x in ENFERMERAS:
        if x.getContra() == password and x.getUsuario() == user:
            return json.dumps(x.__dict__)
    return '{"nombre":"false"}'
#-------------------------------RECETAS------------------------------------------------------------

@app.route('/recetas', methods=['POST'])
def AgregarReceta():
    global RECETAS
    
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']
   

    
    fecha = request.json['fecha']
    paciente = request.json['paciente']
    padecimiento = request.json['padecimiento']
    descripcion = request.json['descripcion']
   
    
        # Creamos nuestro nuevo objeto con la informacion recolectada del request
      
        # Agregamos la persona
       
    RECETAS.append(receta( paciente, fecha,padecimiento,descripcion))
      
        # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})
#-------------------------------FACTURAS--------------------------------------------------------------------------
@app.route('/facturas', methods=['POST'])
def AgregarFactura():
    global FACTURAS
    
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']
   

    
    fecha = request.json['fecha']
    paciente = request.json['paciente']
    doctor = request.json['doctor']
    consulta = request.json['consulta']
    operacion = request.json['operacion']
    internado = request.json['internado']
    total = request.json['total']

    
        # Creamos nuestro nuevo objeto con la informacion recolectada del request
      
        # Agregamos la persona
       
    FACTURAS.append(factura( paciente, fecha,  doctor,consulta, operacion,internado,total))
      
        # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})


# --------------------------------CITAS----------------------------------------------------------------------

@app.route('/citasPaciente/<string:nombre>', methods=['GET'])
def mostrarCitasPacientes(nombre):
    global CITAS
    
    print(nombre)
    print(len(nombre))
    Datos = []
    for Citas in CITAS:
        print(Citas.getPaciente())
        print(len(Citas.getPaciente()))
        #print()
        if Citas.getPaciente().strip() == nombre:
            print("entro al if")
            objeto = {
                'Id': Citas.getId(),
                'Paciente': Citas.getPaciente(),
                'Fecha': Citas.getFecha(),
                'Doctor':  Citas.getDoctor(),
                'Estado':  Citas.getEstado(),
                'Motivo':  Citas.getMotivo(),
                'Hora':  Citas.getHora()
            }
            print(objeto)
            print(len(CITAS))
            
            Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/citasAceptadas/<string:usuario>', methods=['GET'])
def mostrarCitasAceptadasD(usuario):
    global CITAS
    Datos = []
    for Citas in CITAS:
        #print()
        if(Citas.getEstado() == "aceptada") and usuario == Citas.getDoctor():
            objeto = {
                'Id': Citas.getId(),
                'Paciente': Citas.getPaciente(),
                'Fecha': Citas.getFecha(),
                'Doctor':  Citas.getDoctor(),
                'Estado':  Citas.getEstado(),
                'Motivo':  Citas.getMotivo(),
                'Hora':  Citas.getHora()
            }
            print(objeto)
            print(len(CITAS))
            
            Datos.append(objeto)
    return(jsonify(Datos))
@app.route('/citasAceptadas', methods=['GET'])
def mostrarCitasAceptadas():
    global CITAS
    Datos = []
    for Citas in CITAS:
        #print()
        if(Citas.getEstado() == "aceptada"):
            objeto = {
                'Id': Citas.getId(),
                'Paciente': Citas.getPaciente(),
                'Fecha': Citas.getFecha(),
                'Doctor':  Citas.getDoctor(),
                'Estado':  Citas.getEstado(),
                'Motivo':  Citas.getMotivo(),
                'Hora':  Citas.getHora()
            }
            print(objeto)
            print(len(CITAS))
            
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/citasDA/<string:nombre>/<string:doctor>', methods=['PUT'])
def ActualizarCitaDA(nombre,doctor):
    print("llego al python")
    print(doctor)
    # Hacemos referencia a nuestro usuario global
    global CITAS
   
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(CITAS)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if doctor == CITAS[i].getDoctor():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            
          
            CITAS[i].setEstado("completada")
            

            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})

@app.route('/citasD/<string:nombre>/<string:doctor>', methods=['PUT'])
def ActualizarCitaD(nombre,doctor):
    print("llego al python")
    print(doctor)
    # Hacemos referencia a nuestro usuario global
    global CITAS
   
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(CITAS)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if int(nombre) == CITAS[i].getId():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            
            CITAS[i].setDoctor(doctor)
            CITAS[i].setEstado("aceptada")
            

            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})

@app.route('/citas/<string:nombre>', methods=['DELETE'])
def EliminarCitas(nombre):
    print("valor de ID")
    print(nombre)

    # Referencia al arreglo global
    global CITAS
    # Usamos un for para manejar por medio del indice
    for i in range(len(CITAS)):

        print(CITAS[i].getId())
        # Validamos si es el nombre que queremos

        if int(nombre) == CITAS[i].getId():
            print("SON IGUALES")
            # Usamos del para eliminar el objeto
            del CITAS[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje': 'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para eliminar'})


@app.route('/citas/<string:nombre>', methods=['PUT'])
def ActualizarCita(nombre):
    print("llego al python")
    # Hacemos referencia a nuestro usuario global
    global CITAS
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(CITAS)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if int(nombre) == CITAS[i].getId():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            CITAS[i].setId(request.json['id'])
            CITAS[i].setPaciente(request.json['paciente'])
            CITAS[i].setFecha(request.json['fecha'])
            CITAS[i].setDoctor(request.json['doctor'])
            CITAS[i].setEstado(request.json['estado'])
            CITAS[i].setMotivo(request.json['motivo'])
            CITAS[i].setHora(request.json['hora'])

            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})

@app.route('/citas/<string:id>', methods=['GET'])
def mostrarCitass(id):
    global CITAS

    for Citas in CITAS:
        print(Citas.getId())
        print(id)
     
        if(int(id) == Citas.getId()):
            objeto = {
                'Id': Citas.getId(),
                'Paciente': Citas.getPaciente(),
                'Fecha': Citas.getFecha(),
                'Doctor':  Citas.getDoctor(),
                'Estado':  Citas.getEstado(),
                'Motivo':  Citas.getMotivo(),
                'Hora':  Citas.getHora()
            }
            return(jsonify(objeto))

    return(jsonify({'Mensaje': 'no jalo :('}))
@app.route('/citas', methods=['GET'])
def mostrarCitas():
    global CITAS
    Datos = []
    for Citas in CITAS:
        #print()
        if(Citas.getEstado() == "pendiente"):
            objeto = {
                'Id': Citas.getId(),
                'Paciente': Citas.getPaciente(),
                'Fecha': Citas.getFecha(),
                'Doctor':  Citas.getDoctor(),
                'Estado':  Citas.getEstado(),
                'Motivo':  Citas.getMotivo(),
                'Hora':  Citas.getHora()
            }
            print(objeto)
            print(len(CITAS))
            
            Datos.append(objeto)
    return(jsonify(Datos))
    

@app.route('/citascompletas', methods=['GET'])
def mostrarCitasCompletas():
    global CITAS
    Datos = []
    for Citas in CITAS:
        print()
        
        objeto = {
            'Id': Citas.getId(),
            'Paciente': Citas.getPaciente(),
            'Fecha': Citas.getFecha(),
            'Doctor':  Citas.getDoctor(),
            'Estado':  Citas.getEstado(),
            'Motivo':  Citas.getMotivo(),
            'Hora':  Citas.getHora()
        }
        print(objeto)
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Citas', methods=['POST'])
def AgregarCita():
    global CITAS
    global cont 
    cont = cont + 1
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']
    id = cont

    paciente = request.json['paciente']
    fecha = request.json['fecha']
    doctor = request.json['doctor']
    estado = request.json['estado']
    motivo = request.json['motivo']
    hora = request.json['hora']

    if buscarCita(fecha,hora) == "usuario existente":
        return jsonify({'Mensaje': 'el usuario ya existe'})
    else:

        # Creamos nuestro nuevo objeto con la informacion recolectada del request
      
        # Agregamos la persona
       
        CITAS.append(Citas(id, paciente, fecha,  doctor, estado, motivo, hora))
        print(motivo)
        print(len(CITAS))
        # Retornamos nuestro objeto JSON con la salida esperada
        return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})


@app.route('/usuario/<string:id>', methods=['GET'])
def buscarCita(fecha,hora):
    cantUsuarios = 0
    

    global CITAS
    for Citas in CITAS:
        if fecha == Citas.getFecha() and hora == Citas.getHora():
            cantUsuarios = cantUsuarios+1
            print(cantUsuarios)
    if cantUsuarios > 0:
        return("usuario existente")
    else:
        return("nuevo")

# ----------------------------enfermero--------------------------------------------------------------------


@app.route('/enfermeras/<string:usuario>', methods=['GET'])
def BuscarEnfermero(usuario):

    # print(usuario)

    global ENFERMERAS
    for enfermeras in ENFERMERAS:
        print(enfermeras.getnombre())
        if usuario == enfermeras.getUsuario():
            objeto = {
                'Nombre': enfermeras.getnombre(),
                'Apellido': enfermeras.getApellido(),
                'Nacimiento': enfermeras.getNacimieto(),
                'Sexo':  enfermeras.getSexo(),
                'Usuario':  enfermeras.getUsuario(),
                'Contra':  enfermeras.getContra(),
                'Telefono':  enfermeras.getTelefono()
            }
            return(jsonify(objeto))
    salida = {
        "mensaje:": "no se ha encontrado el usuario"

    }
    return(jsonify(salida))


@app.route('/enfermeras/<string:nombre>', methods=['DELETE'])
def EliminarEnfermeras(nombre):
    # Referencia al arreglo global
    global ENFERMERAS
    # Usamos un for para manejar por medio del indice
    for i in range(len(ENFERMERAS)):
        # Validamos si es el nombre que queremos
        if nombre == ENFERMERAS[i].getUsuario():
            # Usamos del para eliminar el objeto
            del ENFERMERAS[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje': 'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para eliminar'})


@app.route('/enfermeras', methods=['GET'])
def mostrarEnfermeros():
    global ENFERMERAS
    Datosd = []
    for enfermeras in ENFERMERAS:
        objetod = {
            'Nombre': enfermeras.getnombre(),
            'Apellido': enfermeras.getApellido(),
            'Nacimiento': enfermeras.getNacimieto(),
            'Sexo':  enfermeras.getSexo(),
            'Usuario':  enfermeras.getUsuario(),
            'contra':  enfermeras.getContra(),
            'telefono':  enfermeras.getTelefono()
        }
        print(objetod)
        Datosd.append(objetod)
    return(jsonify(Datosd))


@app.route('/mostrarEnfermeras', methods=['POST'])
def AgregarEnfermeras():
    global ENFERMERAS

    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']

    nombre = request.json['nombre']
    print(nombre)
    print('leyo el nombre')
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']

    telefono = request.json['telefono']

    if BuscarEnfermero(usuario) == "usuario existente":
        return jsonify({'Mensaje': 'el usuario ya existe'})
    else:

        # Creamos nuestro nuevo objeto con la informacion recolectada del request
        nuevo = enfermeras(nombre, apellido, nacimiento,
                           sexo, usuario, contra, telefono)
        # Agregamos la persona
        ENFERMERAS.append(nuevo)
        # Retornamos nuestro objeto JSON con la salida esperada
        return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})


@app.route('/enfermera/<string:usuario>', methods=['GET'])
def buscarEnfermero(usuario):
    cantUsuarios = 0
    print(usuario)

    global ENFERMERAS
    for enfermeras in ENFERMERAS:
        print(enfermeras.getnombre())
        if usuario == enfermeras.getUsuario():
            cantUsuarios = cantUsuarios+1
            print(cantUsuarios)
    if cantUsuarios > 0:
        return("usuario existente")
    else:
        return("nuevo")


@app.route('/enfermeras/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):
    print("llego al python")
    # Hacemos referencia a nuestro usuario global
    global ENFERMERAS
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(ENFERMERAS)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == ENFERMERAS[i].getnombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            ENFERMERAS[i].setnombre(request.json['nombre'])
            ENFERMERAS[i].setApellido(request.json['apellido'])
            ENFERMERAS[i].setNacimiento(request.json['nacimiento'])
            ENFERMERAS[i].setSexo(request.json['sexo'])
            ENFERMERAS[i].setUsuario(request.json['usuario'])
            ENFERMERAS[i].setContra(request.json['contra'])
            ENFERMERAS[i].setTelefono(request.json['telefono'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})


# --------------------------- Doctores---------------------------------------------------------------------------------


@app.route('/doctores/<string:usuario>', methods=['GET'])
def BuscarDoctor(usuario):

    # print(usuario)

    global Doctores
    for doctores in Doctores:
        print(doctores.getnombre())
        if usuario == doctores.getUsuario():
            objeto = {
                'Nombre': doctores.getnombre(),
                'Apellido': doctores.getApellido(),
                'Nacimiento': doctores.getNacimieto(),
                'Sexo':  doctores.getSexo(),
                'Usuario':  doctores.getUsuario(),
                'Contra':  doctores.getContra(),
                'Especialidad':  doctores.getEspecialidad(),
                'Telefono':  doctores.getTelefono()
            }
            return(jsonify(objeto))
    salida = {
        "mensaje:": "no se ha encontrado el usuario"

    }
    return(jsonify(salida))


@app.route('/doctores/<string:nombre>', methods=['DELETE'])
def EliminarDoctor(nombre):
    # Referencia al arreglo global
    global Doctores
    # Usamos un for para manejar por medio del indice
    for i in range(len(Doctores)):
        # Validamos si es el nombre que queremos
        if nombre == Doctores[i].getUsuario():
            # Usamos del para eliminar el objeto
            del Doctores[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje': 'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para eliminar'})


@app.route('/doctores', methods=['GET'])
def mostrarDoctores():
    global Doctores
    Datosd = []
    for doctores in Doctores:
        objetod = {
            'Nombre': doctores.getnombre(),
            'Apellido': doctores.getApellido(),
            'Nacimiento': doctores.getNacimieto(),
            'Sexo':  doctores.getSexo(),
            'Usuario':  doctores.getUsuario(),
            'contra':  doctores.getContra(),
            'especialidad':  doctores.getEspecialidad(),
            'telefono':  doctores.getTelefono()
        }
        print(objetod)
        Datosd.append(objetod)
    return(jsonify(Datosd))


@app.route('/mostrarDoctores', methods=['POST'])
def AgregarDoctores():
    global Doctores
    print("entra a doctores")
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']

    nombre = request.json['nombre']
    print(nombre)
    print('leyo el nombre')
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']
    especialidad = request.json['especialidad']
    telefono = request.json['telefono']

    if buscarDoctor(usuario) == "usuario existente":
        return jsonify({'Mensaje': 'el usuario ya existe'})
    else:

        # Creamos nuestro nuevo objeto con la informacion recolectada del request
        nuevo = doctores(nombre, apellido, nacimiento,
                         sexo, usuario, contra, especialidad, telefono)
        # Agregamos la persona
        Doctores.append(nuevo)
        # Retornamos nuestro objeto JSON con la salida esperada
        return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})


@app.route('/doctor/<string:usuario>', methods=['GET'])
def buscarDoctor(usuario):
    cantUsuarios = 0
    print(usuario)

    global Doctores
    for doctores in Doctores:
        print(doctores.getnombre())
        if usuario == doctores.getUsuario():
            cantUsuarios = cantUsuarios+1
            print(cantUsuarios)
    if cantUsuarios > 0:
        return("usuario existente")
    else:
        return("nuevo")


@app.route('/doctores/<string:nombre>', methods=['PUT'])
def ActualizarDoctor(nombre):
    print("llego al python")
    # Hacemos referencia a nuestro usuario global
    global Doctores
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(Doctores)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Doctores[i].getnombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Doctores[i].setnombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setNacimiento(request.json['nacimiento'])
            Doctores[i].setSexo(request.json['sexo'])
            Doctores[i].setUsuario(request.json['usuario'])
            Doctores[i].setContra(request.json['contra'])
            Doctores[i].setEspecialidad(request.json['especialidad'])
            Doctores[i].setTelefono(request.json['telefono'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})

# --------------------------------medicamentos-----------------------------------------------


@app.route('/medicamentos', methods=['GET'])
def mostrarMedicamentos():
    global MEDICAMENTOS
    Datosd = []
    for medicamentos in MEDICAMENTOS:
        objetod = {
            'Id': medicamentos.getId(),
            'Nombre': medicamentos.getnombre(),
            'Precio': medicamentos.getPrecio(),
            'Descripcion':  medicamentos.getDescripcion(),
            'Cantidad':  medicamentos.getCantidad(),

        }
        print(objetod)
        Datosd.append(objetod)
    return(jsonify(Datosd))


@app.route('/medicamentos', methods=['POST'])
def AgregarMedicamentos():

    global MEDICAMENTOS

    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']

    id = request.json['id']

    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cantidad = request.json['cantidad']

    if buscarMedicamento(id) == "medicamento existente":
        return jsonify({'Mensaje': 'el usuario ya existe'})
    else:

        # Creamos nuestro nuevo objeto con la informacion recolectada del request
        nuevo = medicamentos(id, nombre, precio, descripcion,
                             cantidad)
        # Agregamos la persona
        MEDICAMENTOS.append(nuevo)
        # Retornamos nuestro objeto JSON con la salida esperada
        return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})


@app.route('/medicamentos/<string:usuario>', methods=['GET'])
def BuscarMedicamento(usuario):

    # print(usuario)

    global MEDICAMENTOS
    for medicamentos in MEDICAMENTOS:

        if int(usuario) == medicamentos.getId():
            objeto = {
                'Id': medicamentos.getId(),
                'Nombre': medicamentos.getnombre(),
                'Precio': medicamentos.getPrecio(),
                'Descripcion':  medicamentos.getDescripcion(),
                'Cantidad':  medicamentos.getCantidad()
            }
            return(jsonify(objeto))
    salida = {
        "mensaje:": "no se ha encontrado el usuario"

    }
    return(jsonify(salida))


@app.route('/medicamentoss/<string:usuario>', methods=['GET'])
def buscarMedicamento(usuario):
    cantUsuarios = 0
    print(usuario)

    global MEDICAMENTOS
    for medicamentos in MEDICAMENTOS:

        if usuario == medicamentos.getId():
            cantUsuarios = cantUsuarios+1
            print(cantUsuarios)
    if cantUsuarios > 0:
        return("Medicamento existente")
    else:
        return("nuevo")


@app.route('/medicamentos/<string:nombre>', methods=['DELETE'])
def Eliminarmedicamentos(nombre):
    print("valor de ID")
    print(nombre)

    # Referencia al arreglo global
    global MEDICAMENTOS
    # Usamos un for para manejar por medio del indice
    for i in range(len(MEDICAMENTOS)):

        print(MEDICAMENTOS[i].getId())
        # Validamos si es el nombre que queremos

        if int(nombre) == MEDICAMENTOS[i].getId():
            print("SON IGUALES")
            # Usamos del para eliminar el objeto
            del MEDICAMENTOS[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje': 'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para eliminar'})


@app.route('/medicamentos/<string:nombre>', methods=['PUT'])
def ActualizarMedicamento(nombre):
    print("llego al python")
    # Hacemos referencia a nuestro usuario global
    global MEDICAMENTOS
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(MEDICAMENTOS)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if int(nombre) == MEDICAMENTOS[i].getId():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            MEDICAMENTOS[i].setId(request.json['id'])
            MEDICAMENTOS[i].setnombre(request.json['nombre'])
            MEDICAMENTOS[i].setPrecio(request.json['precio'])
            MEDICAMENTOS[i].setDescripcion(request.json['descripcion'])
            MEDICAMENTOS[i].setCantidad(request.json['cantidad'])

            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})


# ---------------------------personas-------------------------------------------------------


@app.route('/datosp', methods=['GET'])
def mostrarPersonas():
    global personas
    Datos = []
    for clasePersona in personas:
        objeto = {
            'Nombre': clasePersona.getnombre(),
            'Apellido': clasePersona.getApellido(),
            'Nacimiento': clasePersona.getNacimieto(),
            'Sexo':  clasePersona.getSexo(),
            'Usuario':  clasePersona.getUsuario(),
            'contra':  clasePersona.getContra(),
            'telefono':  clasePersona.getTelefono()
        }
        print(objeto)
        Datos.append(objeto)
    return(jsonify(Datos))

# buscar persona


@app.route('/datosp/<string:nombre>', methods=['GET'])
def buscarPersonas2(nombre):
    print(nombre)

    global personas
    for clasePersona in personas:
        print(clasePersona.getnombre())
        if nombre == clasePersona.getUsuario():
            objeto = {
                'Nombre': clasePersona.getnombre(),
                'Apellido': clasePersona.getApellido(),
                'Nacimiento': clasePersona.getNacimieto(),
                'Sexo':  clasePersona.getSexo(),
                'Usuario':  clasePersona.getUsuario(),
                'Contra':  clasePersona.getContra(),
                'Telefono':  clasePersona.getTelefono()
            }
            return(jsonify(objeto))
    salida = {
        "mensaje:": "no se ha encontrado el usuario"

    }
    return(jsonify(salida))

    # buscar por usuario


@app.route('/usuario/<string:usuario>', methods=['GET'])
def buscarUsuario(usuario):
    cantUsuarios = 0
    print(usuario)

    global personas
    for clasePersona in personas:
        print(clasePersona.getnombre())
        if usuario == clasePersona.getUsuario():
            cantUsuarios = cantUsuarios+1
            print(cantUsuarios)
    if cantUsuarios > 0:
        return("usuario existente")
    else:
        return("nuevo")


@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global personas
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error. #['es lo que va a recibir']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacimiento = request.json['nacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contra = request.json['contra']
    telefono = request.json['telefono']

    if buscarUsuario(usuario) == "usuario existente":
        return jsonify({'Mensaje': 'el usuario ya existe'})
    else:

        # Creamos nuestro nuevo objeto con la informacion recolectada del request
        nuevo = clasePersona(nombre, apellido, nacimiento,
                             sexo, usuario, contra, telefono)
        # Agregamos la persona
        personas.append(nuevo)
        # Retornamos nuestro objeto JSON con la salida esperada
        return jsonify({'Mensaje': 'Se agrego el usuario exitosamente'})
# METODO - ACTUALIZAR UN DATO
# En este caso, vamos a unir los dos conceptos que trabajamos anteriormente para actualizar un dato
# actualizaremos el dato que le mandaremos por el parametro y la nueva informacion se mandara en el body
# NOTA: NO ES OBLIGATORIO USAR UN METODO PUT PARA ACTUALIZAR, SOLO ES POR REFERENCIA


@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    # Hacemos referencia a nuestro usuario global
    global personas
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(personas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == personas[i].getnombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            personas[i].setnombre(request.json['nombre'])
            personas[i].setApellido(request.json['apellido'])
            personas[i].setNacimiento(request.json['nacimiento'])
            personas[i].setSexo(request.json['sexo'])
            personas[i].setUsuario(request.json['usuario'])
            personas[i].setContra(request.json['contra'])
            personas[i].setTelefono(request.json['telefono'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje': 'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para actualizar'})

# METODO - ELIMINAR UN DATO
# En este caso, como trabajaremos con un solo dato, podemos mandar la informacion como parametro.
# NOTA: NO ES NECESARIO UTILIZAR EL METHOD DELETE, ES REFERENCIA UNICAMENTE


@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    # Referencia al arreglo global
    global personas
    # Usamos un for para manejar por medio del indice
    for i in range(len(personas)):
        # Validamos si es el nombre que queremos
        if nombre == personas[i].getnombre():
            # Usamos del para eliminar el objeto
            del personas[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje': 'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje': 'No se encontro el dato para eliminar'})

# NOTA IMPORTANTE: Cabe destacar que el dato que mandamos como parametro debe de ser el identificador del objeto
# Si trabajaramos con un Usuarios, mandamos username, si trabajamos con Recetas, mandamos el correlativo.

# Y POR ULTIMO, CORRER LA APLICACION
# Una vez definido todas nuestras rutas para ser consumidas por un cliente solo nos queda correr la aplicacion


if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
