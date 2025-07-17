class Person():
    """Base class representing a person on campus."""
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"
    
class Student(Person):
    """Represents a student, with major, year, and enrolled courses."""
    def __init__(self, id, name, email, major, year, courses=None):
        super().__init__(id, name, email)
        self.major = major
        self.year = year
        self.courses = courses

    def enroll(self, course):
        self.courses.append(course)
    
    def get_details(self):
        base = super().get_details()
        return f"{base}, Major: {self.major}, Year: {self.year}, Courses enrolled: {self.courses}"

class Faculty(Person):
    """Represents faculty, with department, title, and list of advisees."""
    def __init__(self, name: str, email: str, id_number: str, department: str, title: str, advisees=None):
        super().__init__(name, email, id_number)
        self.department = department
        self.title = title
        self.advisees = advisees or []

    def add_advisee(self, student: Student) -> None:
        self.advisees.append(student)

    def get_details(self) -> str:
        base = super().get_details()
        advisee_names = [s.name for s in self.advisees]
        return f"{base}, Department: {self.department}, Title: {self.title}, Advisees: {advisee_names}"

class Staff(Person):
    """Represents staff, with department, position, and shift hours."""
    def __init__(self, name: str, email: str, id_number: str, department: str, position: str, shift: str):
        super().__init__(name, email, id_number)
        self.department = department
        self.position = position
        self.shift = shift

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base}, Department: {self.department}, Position: {self.position}, Shift: {self.shift}"

# Example usage
if __name__ == "__main__":
    # Create instances
    alice = Student("Alice Smith", "alice@univ.edu", "S123", "Computer Science", 2)
    bob = Faculty("Bob Johnson", "bob@univ.edu", "F456", "Engineering", "Professor")
    carol = Staff("Carol Williams", "carol@univ.edu", "ST789", "Facilities", "Coordinator", "Day")

    # Enroll Alice in a course and add as Bob's advisee
    alice.enroll("Algorithms")
    bob.add_advisee(alice)

    # Print details
    print(alice.get_details())
    print(bob.get_details())
    print(carol.get_details())