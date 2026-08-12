from dataclasses import dataclass


@dataclass
class Complaint:
    complaint_id: str
    student_name: str
    usn: str
    department: str
    category: str
    title: str
    description: str
    location: str
    date: str
    status: str = "Pending"
    priority: str = "Medium"
    technician: str = "Unassigned"
    expected_time: str = "24 hours"
    remarks: str = ""
