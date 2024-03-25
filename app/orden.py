from computadora import Computer
from functools import reduce
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
        listAux=list(reduce(lambda x,y: x+y,self.computers))
        return listAux
        