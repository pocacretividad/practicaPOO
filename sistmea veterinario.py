import datetime

class Medicamento:  #se crea la clase medicamento con atributos nombre y dosis 
                    #y sus respectivos metodos , ver nombre dosis y asignar
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self, med):
        self.__nombre = med 
    
    def asignarDosis(self, med):
        self.__dosis = med 

class Mascota:    #acá se hizo lo mismo con la clase mascota(dar atributos y metodos a la clase)
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    
    def verHistoria(self):
        return self.__historia
    
    def verTipo(self):
        return self.__tipo
    
    def verPeso(self):
        return self.__peso
    
    def verFecha(self):
        return self.__fecha_ingreso
    
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self, n):
        self.__nombre=n
    
    def asignarHistoria(self, nh):
        self.__historia=nh
    
    def asignarTipo(self, t):
        self.__tipo=t
    
    def asignarPeso(self, p):
        self.__peso=p
    
    def asignarFecha(self, f):
        self.__fecha_ingreso=f
    
    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n 
    
    #acá se creó la funcion que permite eliminar los medicamentos
    def eliminarMedicamento(self, nombre_medicamento):
        for medicamento in self.__lista_medicamentos:
            if medicamento.verNombre() == nombre_medicamento:
                self.__lista_medicamentos.remove(medicamento)
                return True
        return False

class SistemaV:
    def __init__(self):
        #esta es un diccionario que contiene a las mascotas segun su tipo.
        
        self.__mascotas_por_tipo = {'canino': [], 'felino': []}
        
        #a partir de este cambio el resto de metodos se reestructuraron para ser usadas en diccionarios
    
    def verificarExiste(self, historia): 
        for tipo_mascota, lista_mascotas in self.__mascotas_por_tipo.items():
            for mascota in lista_mascotas:
                if historia == mascota.verHistoria():
                    return True
        return False
        
    def verNumeroMascotas(self):
        count = 0
        for lista_mascotas in self.__mascotas_por_tipo.values():
            count += len(lista_mascotas)
        return count
    
    def ingresarMascota(self, mascota):
        tipo_mascota = mascota.verTipo().lower()
        self.__mascotas_por_tipo[tipo_mascota].append(mascota) 

    def verFechaIngreso(self, historia):
        for lista_mascotas in self.__mascotas_por_tipo.values():
            for mascota in lista_mascotas:
                if historia == mascota.verHistoria():
                    return mascota.verFecha()
        return None

    def verMedicamento(self, historia):
        for lista_mascotas in self.__mascotas_por_tipo.values():
            for mascota in lista_mascotas:
                if historia == mascota.verHistoria():
                    return mascota.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for tipo_mascota, lista_mascotas in self.__mascotas_por_tipo.items():
            for mascota in lista_mascotas:
                if historia == mascota.verHistoria():
                    lista_mascotas.remove(mascota)
                    return True
        return False 

    def eliminarMedicamentoMascota(self, historia, nombre_medicamento):
        for lista_mascotas in self.__mascotas_por_tipo.values():
            for mascota in lista_mascotas:
                if historia == mascota.verHistoria():
                    return mascota.eliminarMedicamento(nombre_medicamento)
        return False

def main():
    servicio_hospitalario = SistemaV()  #servicio hospitalario se creó como un objeto sistema
    #se añadio la opción de eliminar un medicamento
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de una mascota
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))

            if not servicio_hospitalario.verificarExiste(historia):
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                #la fecha se modificó para que solo acepte el formato de dia , mes y año usando try, except y la libreria date time 
                while True:
                    fecha_str = input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    try:
                        fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y').date()
                        break
                    except ValueError:
                        print("Formato de fecha incorrecto. Inténtelo de nuevo.")

                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(nm):
                    while True:
                        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                        
                        medicamento_existente = False
                        for med in lista_med:
                            if med.verNombre() == nombre_medicamento:
                                print("El medicamento ya está en la lista para esta mascota.")
                                medicamento_existente = True
                                break
                        
                        if not medicamento_existente:
                            break
                    
                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento() #se creo el objeto medicamento, el cual adquierirá estos atributos
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mascota = Mascota() #se creó el objeto mascota , adquirirá estos atributos
                mascota.asignarNombre(nombre)
                mascota.asignarHistoria(historia)
                mascota.asignarPeso(peso)
                mascota.asignarTipo(tipo)
                mascota.asignarFecha(fecha.strftime('%d/%m/%Y'))
                mascota.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mascota) #encapsulamiento
                
            else:
                print("Ya existe la mascota con el número de historia clínica")

        elif menu==2: 
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha is not None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: 
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: 
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento is not None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota: ")

        elif menu == 5: 
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con éxito")
            else:
                print("No se ha podido eliminar la mascota")
        #este es la nueva opción , pedirá la historia como parametro de busqueda, en caso de encontrarla imprimirá una lista
        #con los medicmentos actuales que tiene dicha mascota, se ingresa el nombre del medicamento que se va a borrar y esto se elimina de la lista de esa mascota
        elif menu == 6:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                lista_medicamentos = servicio_hospitalario.verMedicamento(q)
                if lista_medicamentos is not None:
                    print("Los medicamentos actuales de la mascota son:")
                    for index, medicamento in enumerate(lista_medicamentos):
                        print(f"{index + 1}. {medicamento.verNombre()} - Dosis: {medicamento.verDosis()}")
                    
                    nombre_medicamento = input("Ingrese el nombre del medicamento que desea eliminar: ")
                    resultado_operacion = servicio_hospitalario.eliminarMedicamentoMascota(q, nombre_medicamento)
                    if resultado_operacion == True:
                        print("Medicamento eliminado de la mascota con éxito")
                    else:
                        print("No se ha podido eliminar el medicamento de la mascota")
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__=='__main__':
    main()