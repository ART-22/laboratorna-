[OOP.py](https://github.com/user-attachments/files/25542763/OOP.py)
class Human :
    def __init__(self, age= None, name =None, work=None):
        self.__age = age
        self.__name = name
        self.__work = work


    def data (self, new_age = None, new_name =None , new_work=None ):
        self.__age = new_age 
        self.__name = new_name 
        self.__work = new_work
        
    def dani (self):
        print ("age:",self.__age,"\n name:", self.__name , "\n work:", self.__work)

dani_1 =Human()
dani_2 = Human()
dani_2.data(17,"Олександир")
dani_1.data(22,"антон" , "Завод ")
dani_1.dani()
dani_2.dani()




class Student(Human):
    def __init__(self, age=None, name=None, universetet=None):
        super().__init__(age, name, "Навчання")
        self.__universetet =universetet
    def dani(self):
        super().dani() 
        print(f" Universetet:{self.__universetet}")

print("++++++++ клас студент ++++++++ ")
student2 = Student(29, "Андрій ")
student2.dani()
student1 = Student(18, "Олександр", "ЛНУ")
student1.dani()





