from abc import ABC, abstractmethod
from typing import Dict, Any
import uuid

class Person(ABC):
    def __init__(self, name: str, contact_info: Dict[str, str]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.contact_info = contact_info
        self.validate()

    @abstractmethod
    def get_role(self) -> str:
        pass

    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(self.contact_info, dict):
            raise ValueError("Contact info must be a dictionary")
        required_fields = ['email', 'phone']
        for field in required_fields:
            if field not in self.contact_info:
                raise ValueError(f"Contact info must include {field}")

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info,
        }
