from app.models.teacher import Teacher
from typing import Dict

teachers_db = {}

def create_teacher(name: str, contact_info: Dict[str, str], specializations: list) -> Teacher:
    teacher = Teacher(name, contact_info, specializations)
    teachers_db[teacher.id] = teacher
    return teacher

def get_teacher(teacher_id: str) -> Teacher:
    return teachers_db.get(teacher_id)

def update_teacher(teacher_id: str, name: str, contact_info: Dict[str, str], specializations: list) -> Teacher:
    teacher = teachers_db.get(teacher_id)
    if teacher:
        teacher.name = name
        teacher.contact_info = contact_info
        teacher.specializations = specializations
    return teacher

def delete_teacher(teacher_id: str):
    return teachers_db.pop(teacher_id, None)
