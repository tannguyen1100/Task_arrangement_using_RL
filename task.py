class Task():
    __id = 0
    __initTime = 0
    __desComputers = []

    __timeProcess = 0

    def __init__(self, id, initTime = 0):
        self.__id = id
        self.__initTime = initTime
        self.__desComputers = []

    def __str__(self):
        return f"{self.__id}"

    def __repr__(self):
        return str(self)

    def getId(self):
        return self.__id

    def getInitTime(self):
        return self.__initTime

    def getDesComputers(self):
        return self.__desComputers

    def getTimeProcess(self):
        return self.__timeProcess

    def setId(self, id):
        self.__id = id

    def setInitTime(self, initTime):
        self.__initTime = initTime

    def setDesComputers(self, desV):
        self.__desComputers = desV

    def setTimeProcess(self, tProc):
        self.__timeProcess = tProc

    
