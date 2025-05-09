from .person import Person
from typing import List, Dict, Any

class Teacher(Person):
    def __init__(self, name: str, contact_info: Dict[str, str], specializations: List[str]):
        super().__init__(name, contact_info)
        self.specializations = specializations

    def get_role(self) -> str:
        return "teacher"

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict['role'] = 'teacher'
        base_dict['specializations'] = self.specializations
        return base_dict
