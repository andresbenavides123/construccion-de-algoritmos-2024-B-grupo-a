__autor__="ANDRES FELIPE BENAVIDES"
__license__="gpl"
__version__="1.0.0" 
__email__="benavidesandres218@gmail.com"

from Cuentadeahorros import Cuentadeahorros
from Cuentacorriente import Cuentacorriente
from cdt import cdt





class simuladorbancario:

    #__________________________________________________________________
    #Atributos
    #__________________________________________________________________
    cedula=""
    nombre="";

    __Cuentacorriente=Cuentacorriente()
    __Cuentadeahorros=Cuentadeahorros()
    __cdt=cdt()

    __mesActual= 0
    #______________________________________________
    #metodos
    #______________________________________________

__method__="consignecuentacorriente"
__params__="monto"
__returns__="nada"
__descriptions="Este metodo consignar un monto a la cuenta corriente"
def consignacuentacorriente(self,monto):
    #aqui inicia el metodo
    self._cuentacorriente.consignavalor(monto)

__method__="calcularsaldototal"
__params__="ninguno"
__returns__="saldototal"
__descriptions="Este metodo sumo el saldo de todas las cuentas"
def calcularsaldototal(self):
    #aqui inicia el metodo 
    #forma1
    total=self._cuentaCorriente.DarSaldo()+self._Cuentadeahorros.DarSaldo()
    return total

__method__="pasarAhorrosaCorriente"
__params__="ninguno"
__returns__="nada"
__descriptions="Este metodo transfiere el saldo de ahorros a corriente"
def pasarAhorrosaCorriente(self):
    saldotemporal=self._cuentadeahorros.DarSaldo()
    self._cuentadeahorros.RetirarValor(saldotemporal)
    self._Cuentacorriente.ConsignarValor(saldotemporal)

__method__="darsaldo"
__params__="ninguno"
__returns__="saldo"
__descriptions__="Este metodo retorna el saldo"
def darsaldo(self):
    return self._saldo

__method__="ahorro"
__params__="monto"
__returns__="nueva ahorro"
__descriptions__="este metodo transfiere el saldo de la cuenta corriente a la cuenta de ahorros"
def ahorro(self):
    saldotemporalII=self._Cuentacorriente.darsaldo()
    self._Cuentadeahorros.ConsignarValor(saldotemporalII)

    __method__="retirarahorro"
    __params__="monto"
    __returns__="SaldoRestante"
    __descriptions__="Este metodo permite sacar el dinero de la cuenta de ahorros"
    def RetirarTodo(self,monto):
        saldoretirado=self._Cuentacorriente
        self._Cuentacorriente=0
        self._Cuentadeahorros=0

__method__="DuplicarAhorro"
__params__="nada"
__returns__="nada"
__descriptions__="Este metodo nos permite sacar duplicar el valor"
def DuplicarAhorro(self):
    self._Cuentadeahorros=self._Cuentadeahorros+self._Darsaldo()
    




