from employee import Employee
from developer import Developer

class Manager(Employee):
    """The class for all Manager (derived from Employee)"""
    staff = []

    def __init__(self, name, salary):
        super().__init__(name, salary)  # call parent initialiser

    def __str__(self):
     return f"Name: {self.name} Salary: {self.salary} Number of Staff: {len(self.staff)}"

    def add_staff_member(self, developer):
        self.staff.append(developer)
    
    def count_all_java_devs(self):
        count = 0
        for s in self.staff:
            if s.main_dev_language == "Java":
                count = count + 1
        return (count)

    def count_all_py_devs(self):
        count = 0
        for s in self.staff:
            if s.main_dev_language == "Py":
                count = count + 1
        return (count)
    
    def count_all_devs(self):
        return (len(self.staff))

    def java_devs(self):
        java_dev_list = []
        for s in self.staff:
            if s.main_dev_language == "Java":
                java_dev_list.append(s)   
        return java_dev_list

    def py_devs(self):
        return [s for s in self.staff if s.main_dev_language == "Py"]