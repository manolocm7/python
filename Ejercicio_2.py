class Electrodomestico:

    colores = ["blanco", "negro", "rojo", "azul", "gris"]

    consumoEnergeticoLetra = ["A", "B", "C", "D", "E", "F"]

    def __init__(self,precioBase,color,consumoEnergetico,peso):

        self.color=Electrodomestico.comprobarColor(self,color)

        self.precioBase=float(precioBase)

        self.peso=float(peso)

        self.consumoEnergetico = Electrodomestico.comprobarConsumoEnergetico(self,consumoEnergetico)

    def comprobarConsumoEnergetico(self,letra):

        for i in Electrodomestico.consumoEnergeticoLetra:

            if(i==letra):

                return letra

        return "F"

    def comprobarColor(self,color):

        for i in Electrodomestico.colores:

            if(i==color):

                return color

        return "negro"

    def precioFinal(self):

        precioFinal = float(self.precioBase)+float(Electrodomestico.calculoLetras(self,self.consumoEnergetico))

        if self.peso>=0 and self.peso<20:

            precioFinal += 10

        elif self.peso>=20 and self.peso<50:

            precioFinal += 50

        elif self.peso>=50 and self.peso<80:

            precioFinal += 80

        elif self.peso>=80:

            precioFinal += 100

        return precioFinal

    def calculoLetras(self,letra):

        if letra=="A":

            return 100

        elif letra=="B":

            return 80

        elif letra=="C":

            return 60

        elif letra=="D":

            return 50

        elif letra == "D":

            return 30

        elif letra=="D":

            return 10

        else:

            return 0



class Lavadora(Electrodomestico):

    def __init__(self,carga,precioBase,color,consumoEnergetico,peso):

        self.carga=carga

        self.color=Electrodomestico.comprobarColor(self,color)

        self.precioBase=float(precioBase)

        self.consumoEnergetico=Electrodomestico.comprobarConsumoEnergetico(self,consumoEnergetico)

        self.peso=float(peso)

    def getCarga(self):

        return self.carga

    def precioFinal(self):

        precioTotal = Electrodomestico.precioFinal(self)

        if self.carga > 30:

            precioTotal+50

        return precioTotal



class Television(Electrodomestico):

    def __init__(self,resolucion,fourK,precioBase,color,consumoEnergetico,peso):

        self.resolucion=resolucion

        self.fourK=bool(fourK)

        self.color = Electrodomestico.comprobarColor(self,color)

        self.precioBase = float(precioBase)

        self.consumoEnergetico = Electrodomestico.comprobarConsumoEnergetico(self,consumoEnergetico)

        self.peso = float(peso)



    def getResolucion(self):

        return self.resolucion

    def getFourk(self):

        return self.fourK



    def precioFinal(self):

        precioTotal = Electrodomestico.precioFinal(self)

        if self.fourK==True:

            precioTotal+=50

        if self.resolucion>40:

            precioTotal+((precioTotal/100)*30)

        return precioTotal



listaElectro = (Electrodomestico(20,"blanco","A",50),Electrodomestico(320,"blanco","C",20),Television(1024,True,290,"blanco","E",59),Lavadora(30,70,"negro","A",60),Lavadora(50,209,"blanco","A",20),Television(720,False,207,"blanco","A",50),Electrodomestico(225,"blanco","B",100),Electrodomestico(150,"blanco","E",5),Electrodomestico(200,"blanco","C",30),Electrodomestico(40,"negro","B",10))



totalElectrodomestico = 0

totalTelevision = 0

totalLavadora = 0



for i in listaElectro:

    print(i.precioFinal())



for i in listaElectro:

    if type(i) is Electrodomestico:

        totalElectrodomestico += i.precioFinal()

    elif type(i) is Television:

        totalTelevision += i.precioFinal()

    elif type(i) is Lavadora:

        totalLavadora+= i.precioFinal()



print("Precio Electrodomesticos= "+str(totalElectrodomestico))

print("Precio Television= "+str(totalTelevision))

print("Precio Lavadora= "+str(totalLavadora))
