__autor__="Andres felipe benavides bolaños"
__license__="gpl"
__version__="1.0.0" 
__email__="benavidesandres217@gmail.com"

class Fecha:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
     Atributos
    #______________________________________________________________________________'''

    anio = 0 
    mes = 0
    dia = 0

    '''#___________________________________________________________________________
     Metodos
    #______________________________________________________________________________'''

    __method__ = "Dardia"
    __parameter__ = "ninguno"
    __returns__ = "dia"
    __Description__= " metodo que actualiza el dia del empleado"

    def Dardia(self,nuevodia):
        #aqui inicia el codigo

    def Dardia(self):
        #aqui inicia el codigo
        return self.dia 

    __method__ = "Darmes"
    __parameter__ = "ninguno"
    __returns__ = "mes"
    __Description__= " metodo que actualiza el mes del empleado"

    def cambiarmes(self,nuevomes):
        #aqui inicia el codigo

    def Darmes(self):
        #aqui inicia el codigo
        return self.mes 

    __method__ = "Daranio"
    __parameter__ = "ninguno"
    __returns__ = "anio"
    __Description__= " metodo que actualiza el anio del empleado"

    def cambiaranio(self,nuevodia):
        #aqui inicia el codigo

    def Daranio(self):
        #aqui inicia el codigo
        return self.anio
    
    __method__ = "darfecha"
    __parameter__ = "ninguno"
    __returns__ = "fecha de la clase"
    __Description__= "devuelve la fecha de la clase"

    def Darfecha(self):
        #aqui inicia el metodo
        return self.dia+"/"+self.mes+"/"+self.anio