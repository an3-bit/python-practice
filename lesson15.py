#inherintance
#error handling
# dates

class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}")


class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender)
        self.salary = salary
#overide
    def print_salary(self):
        super().print_details()
        print(f"Salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly payment is {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is {self.end_date}")

p1 = PermanentEmployee(name="Jane Smith", id_number=24455645, dob=1989 - 0o2 - 23, gender="F", salary=10000)
p1.print_details()
p1.print_salary()

t1 =TemporaryEmployee("Jin", "22165734", "1995-03-5", "M", 1000,"2024-12-24")
t1.print_details()






