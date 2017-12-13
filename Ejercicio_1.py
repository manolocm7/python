import random

class Persona:

    def __init__(self, nombre,edad,dni,sexo,peso,altura):

        self.nombre = nombre

        self.edad = edad

        self.dni=dni

        self.sexo = sexo

        self.peso=peso

        self.altura=altura



    def calcularIMC(self):

        imc=float(self.peso)/(float(self.altura)*float(self.altura))

        if self.sexo=="H":

            if imc<20:

                return -1,imc

            elif imc>=20 and imc<=25:

                return 0,imc

            elif imc>25:

                return 1,imc

        elif self.sexo=="M":

            if imc<19:

                return -1,imc

            elif imc>=19 and imc<=24:

                return 0,imc

            elif imc>24:

                return 1,imc

    def MayorDeEdad(self):

        if int(self.edad)>=18:

            return True

        else:

            return False

    def introducirSexo(self,sexo):

        if sexo=="H":

            self.sexo=sexo

        else:

            self.sexo="M"

    def toString(self):

        print("Nombre: " + self.nombre)

        print("Edad: " + self.edad)

        print("Dni: " + self.dni)

        print("Sexo: " + self.sexo)

        print("Peso: " + self.peso)

        print("Altura: " + self.altura)

        print()





    def generarDNI(self):

        tablaLetra = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H",

                      "L", "C", "K", "E"]

        for i in range(8):

            numero=random.randint(0,9)

            if(i==0):

                self.dni=str(numero)

            else:

                self.dni=str(self.dni)+str(numero)

        nDni=int(self.dni)

        self.dni=self.dni+"-"+tablaLetra[nDni%23]



def imc(persona):

    a, b = persona.calcularIMC()

    if a==-1:

        print(persona1.nombre+" Esta por debajo de su peso ideal, su imc es: "+str(b))

    elif a==0:

        print(persona1.nombre+" Esta en peso ideal, su imc es: "+str(b))

    elif a==1:

        print(persona1.nombre+" Esta por encima de su peso ideal, su imc es: "+str(b))



def tipoEdad(persona):

    if persona.MayorDeEdad():

        print("Es mayor de edad")

    else:

        print("No es mayor de edad")



nombre=input("Introduzca el nombre: ")

edad=input("Introduzca el edad: ")

sexo=input("Introduzca el sexo: ")

peso=input("Introduzca el peso: ")

altura=input("Introduzca la altura: ")

persona1 = Persona(nombre,edad,None,None,peso,altura)

persona2 = Persona(nombre,edad,None,None,str(80),str(1.80))

persona3 = Persona("Juan",str(23),None,None,str(80),str(1.80))



persona1.introducirSexo(sexo)

persona2.introducirSexo(sexo)

persona3.introducirSexo(sexo)



persona1.generarDNI()

persona2.generarDNI()

persona3.generarDNI()



imc(persona1)

imc(persona2)

imc(persona3)



tipoEdad(persona1)

tipoEdad(persona2)

tipoEdad(persona3)



persona1.toString()

persona2.toString()

persona3.toString()
