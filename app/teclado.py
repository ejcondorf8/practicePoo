from dispositivoentrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    countTeclados = 0
    def __init__(self ,typeInput: str,mark: str):
        super().__init__(typeInput, mark)
        self._idTeclado = Teclado.nextValue()
    @classmethod
    def nextValue(cls):
        cls.countTeclados += 1
        return  cls.countTeclados
    @property
    def idTeclado(self):
        return self._idTeclado
    @idTeclado.setter
    def idTeclado(self, idTeclado):
        raise AttributeError("idTeclado is not editable")
    def __str__(self) -> str:
        return super().__str__() + f"idTeclado: {str(self.idTeclado)}"
    

