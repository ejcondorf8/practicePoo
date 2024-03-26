from computadora import Computer
from functools import reduce
from monitor import Monitor
from raton import Raton
from teclado import Teclado
class Orden():
    countOrden = 0
    @classmethod
    def nextVal(cls):
        cls.countOrden += 1
        return cls.countOrden
    def __init__(self,computers:Computer=[]) -> None:
        self._id=Orden.nextVal()
        self._computers=list(computers)
    @property
    def computers(self):
        return self._computers
    def getTotalPrice(self):
        listAux= [computer.price for computer in self._computers]
        print(listAux)
        return reduce(lambda a,b:a+b,listAux)
    
    def addComputer(self,computer:Computer):
        self._computers.append(computer)
