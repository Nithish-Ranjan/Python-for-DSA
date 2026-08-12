from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base for all system users."""
    def __init__(self, name, email=""):
        self._name, self._email = name, email

    @property
    def name(self): return self._name

    @abstractmethod
    def dashboard_access(self): pass


class Student(Person):
    def __init__(self, name, usn, email=""):
        super().__init__(name, email); self.usn = usn
    def dashboard_access(self): return "submit"


class Technician(Person):
    def __init__(self, name, email="", specialty="General"):
        super().__init__(name, email); self.specialty = specialty
    def dashboard_access(self): return "assigned_complaints"


class Admin(Person):
    def dashboard_access(self): return "all"
