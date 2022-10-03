import yaml
import requests
info = []
conexiones = []
##Informe Previo-Clases
class Alumno:
    def __init__(self,nombre,codigo,PC):
        self.nombre = nombre
        self.codigo = codigo
        self.PC = PC
class Curso:
    def __init__(self,nombre,estado,codigo):
        self.nombre = nombre
        self.estado = estado
        self.codigo = codigo
        self.alumnos = []
        self.servidores = []
    def agregarAlumno (self,alumno):
        self.alumnos.append(alumno)
    def removerAlumno (self,alumno):
        self.alumnos.remove(alumno)
    def agregarServidor(self,servidor):
        self.servidores.append(servidor)
    def removerServidor(self,servidor):
        self.servidores.remove(servidor)
class Servidor:
    def __init__(self,nombre,IP,MAC):
        self.nombre = nombre
        self.IP = IP
        self.MAC = MAC
        self.servicios = []
    def agregarServicio(self,servicio):
        self.servicios.append(servicio)
    def removerServicio(self,servicio):
        self.servicios.remove(servicio)
class Servicio:
    def __init__(self,nombre,protocolo,puerto):
        self.nombre = nombre
        self.protocolo = protocolo
        self.puerto = puerto
class Conexion:
    def __init__(self,handler,usuario,servidor,servicio):
        self.handler = handler
        self.usuario = usuario
        self.servidor = servidor
        self.servicio = servicio
        self.flowEntries = []
    def agregarFlowEntry(self,flowEntry):
        self.flowEntries.append(flowEntry)
    def removerFlowEntry(self,flowEntry):
        self.flowEntries.remove(flowEntry)
##Funciones
def importData(name):
    global info
    try:
        with open(name,"r") as stream:
            try:
                data = yaml.safe_load(stream)
                servidores = data["servidores"]
                cursos = data["cursos"]
                alumnos = data["alumnos"]
                listaCursos = []
                listaAlumnos = []
                listaServidores = []
                listaServicios = []
                for curso in cursos:
                    aux = Curso(curso["nombre"],curso["estado"],curso["codigo"])
                    for alumno in curso["alumnos"]:    
                        aux.agregarAlumno(alumno)
                    for servidor in curso["servidores"]:
                        aux.agregarServidor(servidor["nombre"])
                    listaCursos.append(aux)
                for alumno in alumnos:
                    listaAlumnos.append(Alumno(alumno["nombre"],alumno["codigo"],alumno["mac"]))
                for servidor in servidores:
                    aux = Servidor(servidor["nombre"],servidor["ip"],servidor["mac"])
                    for servicio in servidor ["servicios"]:
                        auxServ = Servicio(servicio["nombre"],servicio["protocolo"],servicio["puerto"])
                        listaServicios.append(auxServ)
                        aux.agregarServicio(auxServ)
                    listaServidores.append(aux)
                print("Data correctamente subida")
                print("Usuarios Importados: "+str(len(listaAlumnos)))
                print("Cursos Importados: "+str(len(listaCursos)))
                print("Servidores Importados: "+str(len(listaServidores)))
                info  = [listaAlumnos,listaCursos,listaServidores,listaServicios]
            except yaml.YAMLError as exc:
                print("El archivo se encuentra dañado ")
    except:
        print("No se encuentra el archivo con nombre "+name)
#Modulo de Cursos
def cursosModulo():
    global info 
    while(True):
        print("-- Cursos --")
        print("Seleccione una opcion: ")
        print("1) Listar")
        print("2) Mostrar Detalle")
        print("3) Actualizar")
        print("-------------------------------")
        print("|Demas Opciones proximamente...")
        print("-------------------------------")
        print("4) Salir")
        opcion = input("Ingrese su opción: ")
        listaCursos = info[1]
        listaServidores = info[2]
        match opcion:
            case "1":
                for curso in listaCursos:
                    print("Nombre del Curso: "+curso.nombre)
                    print("EStado: "+curso.estado)
                    print("Lista de Alumnos: ")
                    for alumno in curso.alumnos:
                        print("- "+str(alumno))
                    print("Lista de Servidores: ")
                    j=0
                    for servidor in curso.servidores:
                        print("- "+servidor)
                        print("Lista de servicios")
                        if(servidor == listaServidores[j].nombre):
                            for servicio in listaServidores[j].servicios:
                                print(".servicio: "+servicio.nombre)
                                print(".protocolo: "+servicio.protocolo)
                                print(".puerto: "+str(servicio.puerto))
                        j+=1
            case "2":
                nombreCurso  = input("Ingrese el nombre del curso o su codigo: ")
                encontrado = False
                for curso in listaCursos:
                    if(nombreCurso == curso.nombre or nombreCurso == curso.codigo):
                        print("Nombre del Curso: "+curso.nombre)
                        print("EStado: "+curso.estado)
                        print("Lista de Alumnos: ")
                        for alumno in curso.alumnos:
                            print("- "+str(alumno))
                        print("Lista de Servidores: ")
                        for servidor in curso.servidores:
                            print("- "+servidor)
                        encontrado = True
                        break
                if(encontrado):
                    print("No se ha encontrado resultados")
            case "3":
                print("Seleccione una opcion: ")
                print("1) Agregar")
                print("2) Eliminar")
                print("3) Salir")
                opcion_Actualizar = input("Ingrese su opción: ")
                curso_Nombre = input("Ingrese el nombre del curso o su codigo: ")
                match = False
                index = 0
                for curso in listaCursos:
                    if(curso_Nombre == curso.nombre or curso_Nombre == curso.codigo):
                        match = True    
                        cursoEditar = curso
                        break                        
                    else:
                        print("No se ha encontrado ese curso en la lista de Cursos!")
                    index += 1
                match opcion_Actualizar:
                    case "1":
                        if(match):
                            CodigoAgregar = input("Digite el codigo del alumno que desea agregar: ")
                            cursoEditar.alumnos.append(int(CodigoAgregar))
                            info[1][index] = cursoEditar
                    case "2":
                        if(match):
                            CodigoEliminar = input("Digite el codigo del alumno que desea eliminar: ")
                            try:
                                cursoEditar.alumnos.remove(int(CodigoEliminar))
                                info[1][index] = cursoEditar
                            except:
                                print("No se ha encontrado al alumno con codigo "+str(CodigoEliminar)+" dentro del curso "+curso.nombre)
                    case "3":
                        break
                    case _:
                        print("Ha ingresado una opcion invalida!")
            case "4":
                break
            case _:
                print("Ha ingresado una opcion incorrecta intente denuevo")  
#Modulo de alumnos
def alumnosModulo():
    global info
    while(True):
        print("-- Alumnos --")
        print("Seleccione una opcion: ")
        print("1) Listar")
        print("2) Mostrar Detalle")
        print("3) Salir")
        print("-------------------------------")
        print("|Demas Opciones proximamente...")
        print("-------------------------------")
        opcion = input("Ingrese su opción: ")
        listaAlumnos  = info[0]
        match opcion:
            case "1":
                for alumno in listaAlumnos:
                    print("Nombre "+alumno.nombre)
                    print("PC MAC:"+alumno.PC)
            case "2":
                nombreAlumno = input("Ingrese el nombre del estudiante o su codigo: ")
                encontrado = False
                for alumno in listaAlumnos:
                    if(alumno.nombre==nombreAlumno or alumno.codigo==nombreAlumno):
                        print("Nombre "+alumno.nombre)
                        print("PC MAC:"+alumno.PC)
                        encontrado = True
                        break
                if(encontrado):
                    print("No se ha encontrado resultados")
            case "3":
                break
            case _:
                print("Ha ingresado una opción inválida por favor intente de nuevo")
#Modulo de Servidores
def servidoresModulo():
    global info
    while(True):
        print("-- Servidores --")
        print("Seleccione una opcion: ")
        print("1) Listar")
        print("2) Mostrar Detalle")
        print("3) Salir")
        print("-------------------------------")
        print("|Demas Opciones proximamente...")
        print("-------------------------------") 
        opcion = input("Ingrese su opción: ")
        listaServidores = info[2]
        match opcion:
            case "1":
                for servidor in listaServidores:
                    print("Servidor: "+servidor.nombre)
                    print("Direccion IP: "+servidor.IP)
            case "2":
                encontrado = False
                nombreBuscar = input("Ingrese el nombre a buscar: ")
                for servidor in listaServidores:
                    if(nombreBuscar==servidor.nombre):
                        print("Servidor: "+servidor.nombre)
                        print("Direccion IP: "+servidor.IP)
                        for servicio in servidor.servicios:
                            print("Servicio: "+servicio.nombre)
                            print("Puerto: "+str(servicio.puerto))
                            print("Protocolo: "+servicio.protocolo)
                        encontrado = True 
                        break
                if(not encontrado):
                    print("No se ha encontrado el servidor con el nombre "+nombreBuscar)
            case "3":
                break
            case _:
                print("Ha ingresado una opcion inválida")
def get_attachment_points(mac):
    api = "http://10.20.12.64:8080/wm/device/"
    response = requests.get(api, params={"mac":mac})
    data = response.json()[0]
    relevantInfo = data["attachmentPoint"][0]
    switchDPID = relevantInfo["switchDPID"]
    outputPort = relevantInfo["port"]
    return[switchDPID, outputPort]
def addflow(flow):
    api = "http://10.20.12.64:8080/wm/staticflowpusher/json"
    response = requests.post(api, json=flow)
    if(response.status_code == 200):
        #print("Flow entry añadida correctamente")
        pass
    else:
        print("Ha ocurrido un error en la flow entry añadida")     
def delflow(flow):
    api = "http://10.20.12.64:8080/wm/staticflowpusher/json"
    response = requests.delete(api, json=flow)
    if(response.status_code == 200):
        #print("Flow entry eliminada correctamente")
        pass
    else:
        print("Ha ocurrido un error en la flow entry eliminada")
def getRoute(DPID_src,port_source,DPID_dest,port_dest,servicio,usuario,servidor):
    listHops = []
    api = "http://10.20.12.64:8080/wm/topology/route/"
    api = api + "/" + DPID_src + "/" + str(port_source) + "/" + DPID_dest + "/" + str(port_dest) + "/json"
    response = requests.get(api)
    data = response.json()
    #print("Ruta del Switch con DPID: "+DPID_src+" hacia el Switch con DPID: "+DPID_dest)
    #print("----------------------------------------------------------------")
    counter = 0
    for hop in data:
        #print(str(counter+1)+". DPID: "+hop["switch"]+" por el puerto: "+str(hop["port"]["portNumber"]))
        counter += 1
        listHops.append([hop["switch"],hop["port"]["portNumber"]])
    #print("----------------------------------------------------------------") 
    #Luego se crean los flows entries tanto para ARP como para los servicios
    listFlowEntries = []
    for counter in range(len(listHops)):
        if counter % 2 == 0 :
            #Estoy en la ida
            flowDirect = {
                "name" : "flowDirect"+str(counter)+": "+servicio.nombre+usuario.PC+"->"+servidor.MAC,
                "switch":listHops[counter][0],
                "cookie":"0",
                "eth_type":"0x0800",
                "ip_proto":"6",
                "eth_src": usuario.PC,
                "eth_dst": servidor.MAC,
                "ipv4_dst": servidor.IP,
                "tp_dst": servicio.puerto,
                "active": "true",
                "actions" : "output="+str(listHops[counter+1][1]) #Mapeo el puerto siguiente
            }
            flowDirectARP={
                "name" : "flowDirectARP"+str(counter)+": "+servicio.nombre+usuario.PC+"->"+servidor.MAC,
                "switch":listHops[counter][0],
                "cookie":"0",
                "eth_type":"0x0806", #ARP
                "arp_opcode":"1", #Request
                "eth_src": usuario.PC,
                "active" : "true",
                "actions" : "output="+str(listHops[counter+1][1])
            }
            listFlowEntries.append(flowDirectARP)
            listFlowEntries.append(flowDirect)
        else:
            #Estoy en la vuelta
            flowBack = {
                "name" : "flowBack"+str(counter)+": "+servicio.nombre+usuario.PC+"->"+servidor.MAC,
                "switch":listHops[counter][0],
                "cookie":"0",
                "eth_type":"0x0800",
                "ip_proto":"6",
                "eth_src": servidor.MAC,
                "ipv4_src": servidor.IP,
                "tp_src": servicio.puerto,
                "eth_dst": usuario.PC,
                "active": "true",
                "actions" : "output="+str(listHops[counter-1][1]) #Mapeo el puerto anterior
            }
            flowBackArp={
                "name" : "flowBackARP"+str(counter)+": "+servicio.nombre+usuario.PC+"->"+servidor.MAC,
                "switch":listHops[counter][0],
                "cookie":"0",
                "eth_type":"0x0806", #ARP
                "arp_opcode":"2", #Reply
                "eth_src": servidor.MAC,
                "active" : "true",
                "actions" : "output="+str(listHops[counter-1][1])
            }
            listFlowEntries.append(flowBackArp)
            listFlowEntries.append(flowBack)
    #Una vez añadidos todos los flow entries se proceden a enviarlo
    for flow in listFlowEntries:
        addflow(flow)
    #Se devuelven los flow entries
    return listFlowEntries
#Modulo de conexiones
def crearConexion(servidor,usuario,curso,servicio):
    estaActivo = False
    estaMatriculado = False
    servidorCurso = False
    servicioServidor = False
    if(curso.estado == "DICTANDO"):
        #Si el curso se encuentra ACTIVO
        estaActivo = True
    if(usuario.codigo in curso.alumnos):
        #Si el codigo del usuario se encuentra dentro de la lista de alumnos del curso
        estaMatriculado = True
    if(servidor.nombre in curso.servidores):
        #Si el servidor se encuentra dentro de la lista de servicio
        servidorCurso = True
    if(servicio in servidor.servicios):
        #Si el servicio que busca se encuentra dentro de los servicios que provee el servidor
        servicioServidor = True
    #Si en caso se tienen todas las validaciones
    if(estaMatriculado and estaActivo and servidorCurso and servicioServidor):
        #Realiza la conexion
        handler = str(usuario.codigo)+"_"+servicio.nombre+"_"+servidor.IP
        conexion = Conexion(handler,usuario.codigo,servidor.IP,servicio.nombre)
        ####
        macUsuario = usuario.PC
        macServidor = servidor.MAC
        #Gestiono los attachmentPoint
        infoSWUsuario = get_attachment_points(macUsuario)
        infoSWServidor = get_attachment_points(macServidor)
        #Obtengo la ruta
        flows = getRoute(infoSWUsuario[0],infoSWUsuario[1],infoSWServidor[0],infoSWServidor[1],servicio,usuario,servidor) 
        for flow in flows:
            conexion.agregarFlowEntry(flow)   
        return conexion
    else:
        print("Hay campos que no coinciden o que son inválidos")
        return "No Match"      
def conexionesModulo():
    global info
    global conexiones
    while(True):
        print("-- Conexiones --")
        print("Seleccione una opcion: ")
        print("1) Crear")
        print("2) Listar")
        print("3) Borrar")
        print("4) Salir")
        print("-------------------------------")
        print("|Demas Opciones proximamente...")
        print("-------------------------------")
        opcion = input("Ingrese su opción: ")
        alumnos = info[0]
        cursos = info[1]
        servidores = info[2]
        servicios = info[3]
        match opcion:
            case "1":
                servidorNombre = input("Ingrese el nombre del Servidor: ")
                alumnoDato = input("Ingrese el nombre o codigo del alumno: ")
                servicioDato = input("Especifique el tipo de servicio: ")
                cursoDato = input("Especifique el codigo o el nombre del curso: ")
                #Verificamos si lo que el usuario ha escrito se encuentra dentro de la base de datos
                alumnoEncontrado = "Algo"
                cursoEncontrado = "Algo"
                servicioEncontrado = "Algo"
                servidorEncontrado = "Algo"
                for alumno in alumnos:
                    if(alumno.nombre == alumnoDato or str(alumno.codigo) == alumnoDato):
                        alumnoEncontrado = alumno                        
                        break
                for curso in cursos:
                    if(curso.nombre == cursoDato or curso.codigo == cursoDato):
                        cursoEncontrado = curso
                        break
                for servicio in servicios:
                    if(servicio.nombre == servicioDato):
                        servicioEncontrado = servicio
                        break
                for servidor in servidores:
                    if(servidor.nombre == servidorNombre):
                        servidorEncontrado = servidor
                        break
                if(servidorEncontrado == "Algo" or servicioEncontrado == "Algo" or alumnoEncontrado == "Algo" or cursoEncontrado == "Algo"):
                    print("No se ha encontrado la informacion ingresada en el sistema")
                else:
                    #Si se ha encontrado toda la data en el sistema se procede a crear la conexion
                    response = crearConexion(servidorEncontrado,alumnoEncontrado,cursoEncontrado,servicioEncontrado)
                    if(response != "No Match" ):
                        conexiones.append(response)
                        print("Conexión creada exitosamente!")
                    else:
                        print("Los campos ingresados son inválidos")
            case "2":
                if(len(conexiones)!= 0):
                    print("# |      Handler     |       Usuario     |      Servidor    |    Servicio   ")
                    counter = 1
                    for conexion in conexiones:
                        print(str(counter)+"."+" |  "+conexion.handler+" | "+str(conexion.usuario)+" | "+conexion.servidor+" | "+conexion.servicio)
                        counter += 1
                else:
                    print("No se tienen conexiones registradas en el sistema!")
            case "3":
                handler = input("Digite el Handler de la conexion que desea eliminar: ")
                if(len(conexiones) != 0):
                    for conexion in conexiones:
                        if(conexion.handler == handler):
                            listFlows = conexion.flowEntries
                            for flow in listFlows:
                                delflow(flow)
                            #Una vez eliminada todos los flows Entries del controlador se borra la conexión de la lista de Conexiones
                            conexiones.remove(conexion)
                            print("Se ha eliminado la conexion correctamente! ")
                            break
                else:
                    print("No hay conexiones registradas para poder eliminar")
            case "4":
                break
            case _:
                print("Ha ingresado una opción invalida")
                print("######################################")
##Menu Principal:                
print("Este proyecto es apto a partir de Python 3.10 en adelante")
print("######################################")
print("Network Policy Manager del UPSM")
print("######################################")
while(True):
    print("-- Menu Principal --")
    print("Seleccione una opcion: ")
    print("1) Importar")
    print("2) Exportar")
    print("3) Cursos")
    print("4) Alumnos")
    print("5) Servidores")
    print("6) Políticas")
    print("7) Conexiones")
    print("8) Salir")
    opcion = input("Ingrese su opción: ")
    match opcion:
        case "1":
            archivo = input("Ingrese el nombre del archivo a importar: ")
            importData(archivo)
        case "2":
            print("Proximamente... ")
        case "3":
            cursosModulo()        
        case "4":
            alumnosModulo()
        case "5":
            servidoresModulo() 
        case "6":
            print("Proximamente... ")
        case "7":
            conexionesModulo()
        case "8" :
            break
        case _:
            print("Ha ingresado una opcion incorrecta intente denuevo")
print("Gracias por usar nuestro servicio!")
print("AgustinVizcarra.Inc")