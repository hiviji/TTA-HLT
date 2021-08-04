from employee import Employee

class Developer(Employee):

    def __init__(self, name, salary, main_dev_language):
        super().__init__(name, salary)  # call parent initialiser
        self.main_dev_language = main_dev_language  

    def __str__(self):
     return f"Name: {self.name} Salary: {self.salary} Lanaguage:{self.main_dev_language}"





