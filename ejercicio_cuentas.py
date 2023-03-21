from datetime import date
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_edad(self):
        return self._edad
   

    def set_edad(self, edad):
        if edad < 0:
            print("La edad debe ser un número positivo")
        else:
            self._edad = edad
            
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        if len(dni) != 8:
            print("El DNI debe tener 8 dígitos")
        else:
            self._dni = dni
            
    def mostrar(self):
        print("Nombre: ", self._nombre)
        print("Edad: ", self._edad)
        print("DNI: ", self._dni)
        
    def es_mayor_de_edad(self):
        return self._edad >= 18
     

class Cuenta:
    def __init__(self,Persona=None, cantidad=None):
        self.__titular = Persona       
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular 

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:")
        self.__titular.mostrar()
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad




class CuentaJoven(Cuenta):
    def __init__(self, Persona, cantidad, bonificacion):
        super().__init__(Persona, cantidad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):       
             
          return True
   
       
    def mostrar_cuenta_joven(self):
         print ("Cuenta Joven ")        
         self.mostrar()
         print( f"Bonificación: {self.bonificacion}%")
 
    def retirar(self, cantidad):
        if not self.es_titular_valido():
            print("El titular de la cuenta no cumple con los requisitos para realizar esta operación.")
          
        super().retirar(cantidad)

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
        
print(f"iniciamos programa")


unapersona = Persona("nina", "47","1111651")
unapersonajoven = Persona("veronica", "27","11115651")
unacuentacomun = Cuenta(unapersona,4)
unacuentajoven = CuentaJoven(unapersonajoven,3,5)

unacuentacomun.mostrar()
unacuentacomun.ingresar(5885)
unacuentacomun.retirar(25)

unacuentajoven.mostrar_cuenta_joven()
unacuentajoven.ingresar(3000)
unacuentajoven.retirar(30)




