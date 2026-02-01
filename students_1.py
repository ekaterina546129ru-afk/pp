
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int


def info(student: Student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def promote(student: Student):
    student.grade += 1
    
def age_check(student: Student) -> bool:
    return student.age >= 18

def compare_students(student1: Student, student2: Student):
    if student1.age > student2.age:
        return f"{student1.name} старше {student2.name}"
    elif student1.age < student2.age:
        return f"{student2.name} старше {student1.name}"
    else:
        return f"{student1.name} и {student2.name} ровесники"
    
def same_class(student1: Student, student2: Student) -> bool:
    return student1.grade == student2.grade

def change_age(student: Student, years: int):
    student.age += years  
    
student1 = Student("Иван", 14, 3)
student2 = Student("Мария", 13, 7)

info(student1)
info(student2)
promote(student1)
info(student1)  