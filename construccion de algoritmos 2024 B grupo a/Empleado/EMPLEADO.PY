__autor__="ANDRES FELIPE BENAVIDES BOLAÑOS"
__license__="gpl"
__version__="1.0.0" 
__email__="benavidesandres217@gmail.com"


from Empleado.Fecha import Fecha 


class Empleado:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
    # Atributos
    #______________________________________________________________________________'''

    nombre="" ""
    apellido="  "
    salario= 0

    '''#___________________________________________________________________________
        # 1 = masculino 2 = femenino
        ____________________________________________________________________________#'''
    sexo = 0
    '''#__________________________________
    #asociasiones
    ________________________#'''

    fechadenacimiento= Fecha()
    fechaingreso= Fecha()
    '''_____________________________________________________________________________
    #METODOS
    ________________________________________________________________________________#'''

    __method__="Cambiar salario"
    __params__="Ninguno"
    __returns__="salario empleado"
    __description__="Devuelve el salario del empleado"

    def Darsalario(self,nuevosalario):
        #aqui inicia el metodo
        return self.salario
    
    __method__="Darsalario"
    __params__="Ninguno"
    __returns__="salario empleado"
    __description__="Devuelve el salario del empleado"

    def Darsalario(self,):
        #aqui inicia el metodo
        return self.salario
    __method__="Aumentosalario"
    __params__="Ninguno"
    __returns__="salario empleado"
    __description__="Devuelve el salario del empleado"

    def Aumentosalario(self,aumento):
        #aqui inicia el metodo
        self.salario=self.salario+aumento
    __method__="calcularsalarioanual"
    __params__="Ninguno"
    __returns__="salario anual"
    __description__="permite aumentar el salario anual del empleado"

    
    def Calcularsalarioanual(self):
        return self.salario*12
    __method__="calcularimpuestosalarialanual"
    __params__="Ninguno"
    __returns__="impuesto del salario anual"
    __description__="permite calcular el impuesto del salario anual del empleado"

    def calcularimpuestoanual(self):
        #aqui inicia el metodo
        salarioanual=self.Calcularsalarioanual()
        return salarioanual*0.19
        #formar 2
        return self.Darsalario()*0,19
    
    __method__="Darfechadeingreso"
    __params__="Ninguno"
    __returns__="Fecha de ingreso"
    __description__="muestra la fecha de ingreso de un empleado"

    def darfechaingreso(self):
        #aqui inicia el metodo
        return self.fechaingreso.Darfecha()
    
    __method__="Darfechanacimiento"
    __params__="Ninguno"
    __returns__="Fecha de nacimiento"
    __description__="muestra la fecha de nacimiento de un empleado"
    
    def Darfechanacimiento(self):
        #aqui inicia el metodo
        return"tu fecha de nacimiento es"+self.fechadenacimiento.Darfecha()
    

    




    

    

    
        


    
    

  