
class Computer():
    __id = 0
    __name = ""


    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def __str__(self):
        return f"{self.__id}"

    def __repr__(self) -> str:
        return self.__str__()

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name


    
