# В.1 SPLIT TEMPORARY VARIABLE (до рефакторингу)
def print_geometry_info_bad(height: float, width: float):
    temp = 2 * (height + width)
    print(f"Периметр: {temp}")
    
    temp = height * width
    print(f"Площа: {temp}")

# В.2 SPLIT TEMPORARY VARIABLE (після рефакторингу)
def print_geometry_info_good(height: float, width: float):
    perimeter = 2 * (height + width)
    print(f"Периметр: {perimeter}")
    
    area = height * width
    print(f"Площа: {area}")


# В.3 REPLACE CONDITIONAL WITH POLYMORPHISM (до рефакторингу)
class EmployeeBad:
    def __init__(self, name: str, emp_type: str):
        self.name = name
        self.emp_type = emp_type

    def calculate_bonus(self, salary: float) -> float:
        if self.emp_type == "Manager":
            return salary * 0.20
        elif self.emp_type == "Developer":
            return salary * 0.15
        elif self.emp_type == "Tester":
            return salary * 0.10
        else:
            return 0.0

# В.4 REPLACE CONDITIONAL WITH POLYMORPHISM (після рефакторингу)
class Employee:
    def __init__(self, name: str):
        self.name = name

    def calculate_bonus(self, salary: float) -> float:
        return 0.0

class Manager(Employee):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.20

class Developer(Employee):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.15

class Tester(Employee):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.10


# В.5 SUBSTITUTE ALGORITHM (до рефакторингу))
def found_person_bad(people: list[str]) -> str:
    for i in range(len(people)):
        if people[i] == "Vanya":
            return "Vanya"
        if people[i] == "John":
            return "John"
        if people[i] == "Denys":
            return "Denys"
    return ""

# В.6 SUBSTITUTE ALGORITHM (після рефакторингу)
def found_person_good(people: list[str]) -> str:
    candidates = ["Vanya", "John", "Denys"]
    for person in people:
        if person in candidates:
            return person
    return ""
