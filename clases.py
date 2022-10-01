#self -> Hace referencia a la instancia que esta siendo llamada en ese instante
class Alumno:
    def __init__(self,nombre,PC):
        self.nombre = nombre
        self.PC = PC
class Curso:
    def __init__(self,nombre,estado) -> None:
        self.nombre = nombre
        self.estado = estado
        #Los atributos ya instanciados se definen dentro de la clase
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
    def __init__(self,nombre,IP):
        self.nombre = nombre
        self.IP = IP
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
if __name__ == '__main__':
#Se instanciará las clases
    s1 = Servicio("MailSender","ICMP","6")
    server1 = Servidor("API","10.20.11.64")
    #Se añade el servicio al servidor
    server1.agregarServicio(s1)
    print("El Servidor cuenta con servicios" if len(server1.servicios) != 0 else "El servidor se encuentra vacio")
    alumno1 = Alumno("Agustin Vizcarra","10:ec:4e:fg:00:er")
    alumno2 = Alumno("Carlos Aguinaga","10:ec:4e:fg:00:ej")
    alumno3 = Alumno("Joaquin Aragon","10:ec:4e:fg:00:em")
    curso1 = Curso("Redes Definidas por Software","activo")
    #Se añade el alumno al curso
    curso1.agregarAlumno(alumno1)
    curso1.agregarAlumno(alumno2)
    curso1.agregarAlumno(alumno3)
    print("El curso "+curso1.nombre+ " cuenta con "+str(len(curso1.alumnos))+" alumnos")
    #Se elimina alumnos
    curso1.removerAlumno(alumno2)
    print("El curso "+curso1.nombre+ " cuenta con "+str(len(curso1.alumnos))+ " alumnos")
        
        
