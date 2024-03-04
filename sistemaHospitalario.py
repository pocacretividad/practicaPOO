class Paciente:      #creación de la clase 
    def __init__(self):   #método constructor y sus respectivos atributos
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    # Métodos get    
    def verNombre(self):
        return self.__nombre 
    
    def verCedula(self):
        return self.__cedula 
    
    def verGenero(self):
        return self.__genero 
    
    def verServicio(self):
        return self.__servicio 
    
    # Métodos set
    def asignarNombre(self, n):
        self.__nombre = n 
    
    def asignarCedula(self, c):
        self.__cedula = c 
    
    def asignarGenero(self, g):
        self.__genero = g 
    
    def asignarServicio(self, s):
        self.__servicio = s 
        
class Sistema:    #creacion clase sistema 
    def __init__(self):  #método constructor
        self.__lista_pacientes = [] #los atributos de paciente serán guardados en esta lista que es el atributo de sistema
    #metodos de la clase sistema   
    def verificarPaciente(self, cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
        
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
        return True
    #nuevo método que permite eliminar un paciente registrado si se encuentra su cédula
    def eliminarPaciente(self, cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                self.__lista_pacientes.remove(p)
                return True
        return False
    #con este se verifica si el paciente esta en el sistema mediante su cédula y la devuelve
    def verDatosPaciente(self, cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return p 
        return None
    
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 
def main():
    sis = Sistema() 
    #se creó un menú mas completo al de la version 3 añadiendo las opciones de eliminar y ver datos de un paciente
    while True:
        print("\menú:")
        print("0 - Salir")
        print("1 - Ingresar un nuevo paciente")
        print("2 - Ver datos de un paciente")
        print("3 - Eliminar un paciente")
        print("4 - Ver cantidad de pacientes en el sistema")
        
        opcion = int(input("seleccione la opción deseada: ")) 
        
        if opcion == 1:
            print("ingrese los siguientes datos") 
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print(" Ya existe un paciente con esa cedula") 
            else:    
                pac = Paciente() 
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            cedula = int(input("Ingrese la cedula del paciente: ")) 
            paciente = sis.verDatosPaciente(cedula) 
            if paciente is not None:  #si el paciente se encuntra en el sistema se usarán los getters para obetner dicha info
                print("los datos del paciente son:")
                print("Nombre: " + paciente.verNombre()) 
                print("Cedula: " + str(paciente.verCedula())) 
                print("Genero: " + paciente.verGenero()) 
                print("Servicio: " + paciente.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion == 3:
            cedula = int(input("Ingrese la cedula del paciente a eliminar: ")) 
            if sis.eliminarPaciente(cedula):  #se usa el metodo nuevo 
                print("Paciente eliminado ")
            else:
                print("No se encontró un paciente con esa cedula")
        elif opcion == 4:
            sis.verNumeroPacientes()
        else:
            break 

if __name__ == "__main__":
    main() 
    
    #en este ejercicio no se presentó herencia ni polimorfismos 