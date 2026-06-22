class Student:
    def __init__(self,name,grade):
        self.name = name 
        self.grade = grade

    def __str__(self):
        return f"Student(Name of the Student: {self.name}, Grade of the Student: = {self.grade})"
    
    def __repr__(self):
        return f"Student(Name = '{self.name}', Grade = '{self.grade}')"
    
    def __eq__(self,other):
        return self.name == other.name and self.grade == other.grade 


student1 = Student("Prapti", "A")
student2 = Student("Aditya", "A")
student3 = Student("Prapti", "A")

print(student1 == student3)
print(student1 == student2)
print(student1)
print([student1, student2])

