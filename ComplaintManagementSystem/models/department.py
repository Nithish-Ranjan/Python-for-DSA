from dataclasses import dataclass


@dataclass
class Department:
    name: str
    contact: str = ""
    description: str = ""
