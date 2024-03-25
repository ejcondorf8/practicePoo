from dispositivoentrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    countRatones = 0
    @classmethod
    def nextValue(cls):
        cls.countRatones += 1
        return  cls.countRatones 

    def __init__(self ,typeInput: str,mark: str):
        super().__init__(typeInput, mark)
        self._idRaton = Raton.nextValue()

    @property
    def idRaton(self):
        return self._idRaton
    @idRaton.setter
    def idRaton(self, idRaton):
        raise AttributeError("idRaton is not editable")
    def __str__(self) -> str:
        return super().__str__() + f"idRaton: {str(self.idRaton)}"
    



if __name__ == "__main__":
    raton = Raton("usb","hp")
    print(raton)