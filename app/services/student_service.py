from app.models.student import Student
from typing import Dict

students_db = {}

def create_student(name: str, contact_info: Dict[str, str]) -> Student:
    student = Student(name, contact_info)
    students_db[student.id] = student
    return student

def get_student(student_id: str) -> Student:
    return students_db.get(student_id)

def get_all_students() -> list:

    return [student.to_dict() for student in students_db.values()]


def update_student(student_id: str, name: str, contact_info: Dict[str, str]) -> Student:
    student = students_db.get(student_id)
    if student:
        student.name = name
        student.contact_info = contact_info
    return student

def delete_student(student_id: str):
    return students_db.pop(student_id, None)
