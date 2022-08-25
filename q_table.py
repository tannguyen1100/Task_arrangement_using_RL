class QTable():
    __id = 0
    __label = ""
    __computer = None
    __task = None
    __tProc = 0
    __value = 0

    def __init__(self, id, computer, task, tProc=0, value=0):
        self.__id = id
        self.__computer = computer
        self.__task = task
        self.__tProc = tProc
        self.__value = value
        self.__label = f"{task.getId()}{computer.getId()}"

    def __str__(self):
        return f"{self.__label}_{self.__tProc}_{self.__value}"

    def __repr__(self) -> str:
        return self.__str__()
    
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getTask(self):
        return self.__task

    def setTask(self, task):
        self.__task = task

    def getComputer(self):
        return self.__computer

    def setComputer(self, computer):
        self.__computer = computer

    def getLabel(self):
        return self.__label

    def getTProc(self):
        return self.__tProc

    def setTProc(self, tProc):
        self.__tProc = tProc

    def getValue(self):
        return round(self.__value, 3)

    def setValue(self, value):
        self.__value = value