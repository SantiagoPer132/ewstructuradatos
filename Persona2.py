class Persona2:
    def _init_(self):
        self.nombre=input("ingrese el nombre:")
        self.apellidos=input("ingrese sus apellidos:")
    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)

class Alumnos(Persona2):
    def _init_(self):
        super()._init_()
        self.matriula=input("Ingrese la matricula: ")

    def mostrarAlumno(self):
        super().mostrar()
        print("Matricula: ", self.matriula)

#Alumnos=Persona2()
#Alumnos.mostrar()
Alumno1=Alumnos()
Alumnos.mostrarAlumno()