#LinhMTT
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.__email = email

    @abstractmethod
    def display_info(self):
        pass

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

class Student(Person):
    def __init__(self, name, age, email, student_id, grades):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.grades = grades

    def calculate_gpa(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def display_info(self):
        print(
            f'''----------Information of {self.name}---------
            Student_ID: {self.student_id}
            Name: {self.name}
            Age: {self.age}
            Email: {self.get_email()}
            GPA: {self.calculate_gpa()}
            '''
        )

class Teacher(Person):
    def __init__(self, name, age, email, employee_id, student_list):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.student_list = student_list

    def calculate_students_gpa(self):
        gpa_list = []
        for student in self.student_list:
            gpa = student.calculate_gpa()
            gpa_list.append(gpa)
        
        return sum(gpa_list) / len(gpa_list)
    
    def display_info(self):
        print(
            f'''----------Information of {self.name}---------
            Employee_ID: {self.employee_id}
            Name: {self.name}
            Age: {self.age}
            Email: {self.get_email()}
            Average GPA of students: {self.calculate_students_gpa()}
            '''
        )

s1 = Student("Linh", 30, "linh@gmail.com", "ST123", {"Math": 5, "English": 8, "Physics": 5})
s2 = Student("Vy", 28, "vy@gmail.com", "ST123444", {"Math": 10, "English": 8})
s3 = Student("Thang", 25, "thang@gmail.com", "ST123566", {"Math": 7, "Physics": 8})
s4 = Student("Duc", 21, "duc@gmail.com", "ST5636", {"Math": 6, "English": 5, "Physics": 5})
s1.display_info()
s2.display_info()
s3.display_info()
s4.display_info()

t1 = Teacher("Phuc", 29, "phuc@gmail.com", "TE10884", [s1, s2])
t2 = Teacher("Uyen", 35, "uyen@gmail.com", "TE10222", [s3, s4])
t1.display_info()
t2.display_info()