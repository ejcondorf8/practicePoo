from monitor import Monitor
from raton import Raton
from teclado import Teclado

class Computer:
    countComputer = 0
    @classmethod
    def nextValue(cls):
        cls.countComputer += 1
        return  cls.countComputer
    def __init__(self,monitor:Monitor,raton:Raton,teclado:Teclado,price:int,name:str) -> None:
        self._id=Computer.nextValue()
        if self.__checkTypes(monitor,raton,teclado):
            self._monitor=monitor
            self._raton=raton
            self._teclado=teclado
        else:
            raise TypeError("monitor, raton, teclado, price and name must be Monitor, Raton, Teclado, int and str")
        self._price=price
        self._name=name
    def __checkTypes(self,monitor,raton,teclado):
        return True if isinstance(monitor, Monitor) and isinstance(raton, Raton) and isinstance(teclado, Teclado) else False
    def __str__(self) -> str:
        return f"id: {str(self.id)} monitor: {str(self.monitor)} raton: {str(self.raton)} teclado: {str(self.teclado)} price: {str(self.price)} name: {self.name}"
    @property
    def id(self):
        return self._id
    @property
    def monitor(self):
        return self._monitor
    @property
    def raton(self):
        return self._raton
    @property
    def teclado(self):
        return self._teclado
    @property
    def price(self):
        return self._price
    @property
    def name(self):
        return self._name
    @price.setter
    def price(self,price):
        self._price=price
    @name.setter
    def name(self,name):
        self._name=name
    @monitor.setter
    def monitor(self,monitor):
        self._monitor=monitor
    @raton.setter
    def raton(self,raton):
        self._raton=raton
    @teclado.setter
    def teclado(self,teclado):
        self._teclado=teclado

if __name__=="__main__":
    monitor1=Monitor("hp",15.5)
    teclado1=Teclado("usb","hp")
    raton1=Raton("usb","hp")
    computer1=Computer(monitor1,raton1,teclado1,1000,"hp")
    print(computer1)
    
        