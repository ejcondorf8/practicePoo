
class Monitor():
    countMonitor=0
    @classmethod
    def nextValue(cls):
        cls.countMonitor += 1
        return  cls.countMonitor
    def __init__(self,mark:str,sizeComputer:float) -> None:
        self._id=Monitor.nextValue()
        if self.__checkTypes(mark,sizeComputer):
            self._mark=mark
            self._sizeComputer=sizeComputer
        else:
            raise TypeError("mark and sizeComputer must be str and float")

    
    def __str__(self) -> str:
        return f"id: {str(self.id)} mark: {self.mark} sizeComputer: {str(self.sizeComputer)}"
    @property
    def id(self):
        return self._id
    @property
    def mark(self):
        return self._mark
    @property
    def sizeComputer(self):
        return self._sizeComputer
    @id.setter
    def id(self,id):
        raise AttributeError("id is not editable")
    def __checkTypes(self, mark: str, sizeComputer: float):
        return True if isinstance(mark, str) and isinstance(sizeComputer, float) else False    

if __name__=="__main__":
    monitor1=Monitor("hp",15.5)
    print(monitor1)