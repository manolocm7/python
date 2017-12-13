class Serie:

    def __init__(self,titulo,nTemporada,genero,creador):

        self.titulo=titulo

        self.nTemporadas=nTemporada

        self.entregado=False

        self.genero=genero

        self.creador=creador

    def getTitulo(self):

        return self.titulo

    def getNTemporadas(self):

        return self.nTemporadas

    def getGenero(self):

        return self.genero

    def getCreador(self):

        return self.creador



    def setTitulo(self,titulo):

        self.titulo=titulo

    def setNTemporadas(self,nTemporadas):

        self.nTemporadas=nTemporadas

    def setGenero(self,genero):

        self.genero=genero

    def setCreador(self,creador):

        self.creador=creador



    def entregar(self):

        if self.entregado == False:

            self.entregado=True

        else:

            self.entregado=False



class Videojuego:

    def __init__(self,titulo,horasEstimadas,genero,compania):

        self.titulo=titulo

        self.horasEstimadas=horasEstimadas

        self.entregado=False

        self.genero=genero

        self.compania=compania



    def getTitulo(self):

        return self.titulo



    def getHorasEstimadas(self):

        return self.horasEstimadas



    def getGenero(self):

        return self.genero



    def getCompania(self):

        return self.compania



    def setTitulo(self, titulo):

        self.titulo = titulo



    def setHorasEstimadas(self, horasEstimadas):

        self.horasEstimadas = horasEstimadas



    def setGenero(self, genero):

        self.genero = genero



    def setCompania(self, compania):

        self.compania = compania



    def entregar(self):

        if self.entregado == False:

            self.entregado=True

        else:

            self.entregado=False



listSeries=(Serie("Flash",2,"Accion","desconocido"),Serie("Prison Break",4,"Aventura","Desconocido"),Serie("Juego de Tronos",7,"Accion","Desconocido"),Serie("Juego de Tronos",6,"Accion","Desconocido"),Serie("Arrow",5,"Accion","Desconocido"))



listVideojuegos=(Videojuego("Call of duty w3",20,"Accion","Accion Activity"),Videojuego("Call of dutty w2",20,"Accion","Accion Activity"),Videojuego("Call of dutty Black ops",20,"Accion","Accion Activity"),Videojuego("Call of dutty Black ops 2",20,"Accion","Accion Activity"),Videojuego("Call of dutty Black ops 3",20,"Accion","Accion Activity"))



listSeries.__getitem__(0).entregar()

listSeries.__getitem__(4).entregar()

listVideojuegos.__getitem__(1).entregar()

listVideojuegos.__getitem__(3).entregar()



countSeries = 0

countVideojuegos = 0

for i in listVideojuegos:

    if i.entregado == True:

        countVideojuegos+=1

        i.entregar()



for i in listSeries:

    if i.entregado == True:

        countSeries+=1

        i.entregar()



print("Hay "+str(countSeries)+" Series Entregadas")

print("Hay "+str(countVideojuegos)+" Juegos entregados")



maxTemporada = 0

maxHoras = 0

nomMaxSerie=""

nomMaxVideoJuego=""



for i in listSeries:

    if i.getNTemporadas()>maxTemporada:

        maxTemporada=i.getNTemporadas()

        nomMaxSerie=i.getTitulo()



for i in listVideojuegos:

    if i.getHorasEstimadas()>maxHoras:

        maxHoras=i.getHorasEstimadas()

        nomMaxVideoJuego = i.getTitulo()



print("El videojuego con mas horas es: "+nomMaxVideoJuego)

print("La serie con mas temporadas es: "+nomMaxSerie)
