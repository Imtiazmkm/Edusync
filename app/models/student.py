from .person import Person
from typing import Dict, Any

class Student(Person):
    def __init__(self, name: str, contact_info: Dict[str, str]):
        super().__init__(name, contact_info)
        self.enrolled_courses = set()

    def get_role(self) -> str:
        return "student"

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict['role'] = 'student'
        base_dict['enrolled_courses'] = list(self.enrolled_courses)
        return base_dict
