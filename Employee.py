from person import person
from abc import ABC,abstractmethod
class employee(person,ABC):
    def __init__(self,name):
        super().__init__(name)
        self.__salary = None
        self.__rank = None
        self.__job=  None

    def setSalary(self,salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def setRank(self,rank):
        self.__rank = rank

    def getRank(self):
        return self.__rank

    def setJob(self,job):
        self.__job = job

    def getJob(self):
        return self.__job



