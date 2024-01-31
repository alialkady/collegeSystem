class person():
    def __init__(self,name :str):
        self.__name = name
        self.__age = None
        self.__address = None
        self.__nationality = None

    def setAge(self,age:int):
        if age>=20:
            self.__age = age
        else:
            print("we don't hire under 20")

    def getAge(self):
        return self.__age

    def setAddress(self,address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def setNationality(self,nationality):
        self.__nationality = nationality

    def getNationality(self):
        return self.__nationality


