"""
While not fundamentally different to the Person.py class (actually it's the exact same code, except the different parent class name),
the reason I felt OnCampus would be better was since OnCampus is better utilised when designing for a hierarchy of a college campus. 
That means that it's more defined in terms of domain clarity instead of "Person" which is too generic. 

Aside from that I asked GPT for some system design consideration when designing such a hierarchy, and it said the following:
## Low-level system design considerations
    Even small hierarchies benefit from design principles:

- Single Responsibility: Each class handles its own data and behavior (e.g., enrollment belongs in Student).

- Open/Closed: New roles (e.g., Visitor, Contractor) can be added without modifying existing classes—just subclass OnCampus.

- Liskov Substitution: Anywhere you accept an OnCampus instance, you should be able to use a Student, Faculty, or Staff without surprises.

- Composition over Inheritance: If roles share behavior only partially (e.g., both Faculty and Staff have department), consider a mixin or a separate Departmental component instead of pushing everything into one deep hierarchy.

- Persistence & Lifecycle: In a real system, think about how objects map to database tables (ORM), caching, and identity (e.g., ensuring id_number uniqueness).
(Scroll to the end for deeper explanation of the last two points.)
"""
class OnCampus():
    """Base class representing a person on campus."""
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"
    
class Student(OnCampus):
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

class Faculty(OnCampus):
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

class Staff(OnCampus):
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

"""
1. Composition over Inheritance

    The problem with deep hierarchies: When you force every subclass to inherit all attributes of the parent—even if they don’t all use them—you end up with fragile, inflexible designs. For example, both Faculty and Staff share a department, but Student does not. Forcing Student to inherit department would be semantically wrong.

    Composition (has-a) instead of inheritance (is-a): Extract the shared concerns into their own small classes (or mixins) and compose them into your main classes.

    ---------------------------------------------------------------------
    python code:
        class Departmental:
            def __init__(self, department: str):
                self.department = department

        class Faculty(OnCampus, Departmental): ...
        class Staff(OnCampus, Departmental): ...
    ---------------------------------------------------------------------
    
        Here, Departmental is a mixin providing only department. You avoid “polluting” Student with unused attributes, and you keep each piece of functionality in a focused, reusable component.

2. Persistence & Lifecycle
    In a real-world system, your in-memory objects usually map to database rows, get cached, and need unique, stable identities.

    ORM mapping:

        Each class corresponds to a database table.

        Fields like id_number become primary keys.

        You add metadata or decorators (e.g., with SQLAlchemy or Django ORM) to specify column types, uniqueness constraints, and relationships.

    Identity & Uniqueness:

        Ensure id_number (or a surrogate uuid) is unique at the database level.

        Avoid having two objects in memory with the same identity—use an identity map or session cache.

    Lifecycle hooks:

        On creation: validate data (e.g., email format), assign defaults.

        On update: enforce business rules (e.g., a student can’t enroll after graduation).

        On deletion or archival: soft-delete (mark inactive) vs. cascade-delete related records.

    Caching:

        Frequently accessed objects (e.g., a faculty’s advisee list) can be cached in an LRU or Redis.

        Invalidate caches on mutation (e.g., when a new advisee is added).

"""