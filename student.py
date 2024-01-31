from person import person
class student(person):
    def __int__(self,name):
        super().__int__(name)
        self.__study_level = None
        self.__speciallization = None
        self.__gpa = None

    def setStudyLevel(self,level:int):
        self.__study_level = level

    def getStudyLevel(self):
        return self.__study_level

    def setSpeciallization(self,specillization:str):
        self.__speciallization = specillization

    def getSpecillization(self):
        return self.__speciallization

    def setGpa(self,gpa:float):
        self.__gpa =gpa
    def getGpa(self):
        return self.__gpa


