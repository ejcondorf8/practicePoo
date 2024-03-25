class DispositivoEntrada:
    def __init__(self ,typeInput: str,mark: str):
        if self.__checkTypes(typeInput, mark):
            self._typeInput = typeInput
            self._mark= mark
        else:
            raise TypeError("typeInput and mark must be str")
    @property
    def typeInput(self):
        return self._typeInput
    @property
    def mark(self):
        return self._mark
    @typeInput.setter
    def typeInput(self, typeInput):
        self._typeInput = typeInput
    @mark.setter
    def mark(self, mark):
        self._mark = mark
    
    def __checkTypes(self, typeInput: str, mark: str):
        return True if isinstance(typeInput, str) and isinstance(mark, str) else False
    def __str__(self) -> str:
        return f"typeInput: {self.typeInput} mark: {self.mark}"
