class Employee:
    def __init__(self,emp_id,emp_name,emp_designation):
        self.emp_id=emp_id
        self.emp_name = emp_name
        self.emp_designation= emp_designation
    def emp_info(self):
        print("Employee Id--->",self.emp_id)
        print("Employee Name--->",self.emp_name)
        print("Employee designation--->",self.emp_designation)

emp_obj=Employee(5080180,'Anu','developer')
emp_obj.emp_info()

